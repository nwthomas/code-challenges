from copy import deepcopy
from dataclasses import dataclass, field
from heapq import heappop, heappush
from typing import List, Optional


@dataclass
class Transaction:
    """
    Preserves a grant creation, subtract, or get_balance transaction
    at a given point in time
    """

    action: str
    amount: int
    timestamp: int
    expiration_timestamp: Optional[int]

    def __init__(
        self,
        action: str,
        timestamp: int,
        amount: int,
        expiration_timestamp: Optional[int],
    ):
        self.action = action
        self.amount = amount
        self.timestamp = timestamp
        self.expiration_timestamp = expiration_timestamp

    def __lt__(self, other_value) -> bool:
        return self.expiration_timestamp < other_value.expiration_timestamp


@dataclass
class GPUCreditTracker:
    """
    Implements the ability to create GPU credit grants, subtract credits, and get the credit
    balance at a given point in time.
    """

    transactions: List[Transaction] = field(default_factory=list)

    def create_grant(
        self, timestamp: int, expiration_timestamp: int, amount: int
    ) -> None:
        """Creates a grant for a credit balance increase"""
        transaction = Transaction("grant", timestamp, amount, expiration_timestamp)
        self.__insert_transaction(transaction)

    def subtract(self, timestamp: int, amount: int) -> None:
        """Subtracts credits from the current balance if possible"""
        transaction = Transaction("subtract", timestamp, amount, None)
        self.__insert_transaction(transaction)

    def get_balance(self, timestamp: int) -> int:
        """Returns the balance at a certain point in time"""
        grant_heap = []
        current = 0

        while (
            current < len(self.transactions)
            and self.transactions[current].timestamp <= timestamp
        ):
            current_transaction = deepcopy(self.transactions[current])

            # Clear out stale grants that have expired and can no longer be used
            while (
                len(grant_heap) > 0
                and grant_heap[0].expiration_timestamp < current_transaction.timestamp
            ):
                heappop(grant_heap)

            if current_transaction.action == "grant":
                heappush(grant_heap, current_transaction)
            elif current_transaction.action == "subtract":
                total_subtract_remaining = current_transaction.amount

                while len(grant_heap) > 0 and total_subtract_remaining > 0:
                    current_grant_remaining_amount = grant_heap[0].amount

                    if current_grant_remaining_amount >= total_subtract_remaining:
                        grant_heap[0].amount -= total_subtract_remaining
                        total_subtract_remaining = 0
                    else:
                        total_subtract_remaining -= grant_heap[0].amount
                        heappop(grant_heap)

            current += 1

        total = 0
        while len(grant_heap) > 0:
            current_grant = heappop(grant_heap)

            if current_grant.expiration_timestamp > timestamp:
                total += current_grant.amount

        return total if total > 0 else 0

    def __insert_transaction(self, transaction: Transaction) -> None:
        if len(self.transactions) == 0:
            self.transactions.append(transaction)
        else:
            current = 0

            while current < len(self.transactions) and (
                (
                    # Place grant transactions at beginning of same timestamp
                    transaction.action == "grant"
                    and self.transactions[current].timestamp < transaction.timestamp
                )
                or (
                    # Place subtract transactions at end of same timestamp
                    transaction.action == "subtract"
                    and self.transactions[current].timestamp <= transaction.timestamp
                )
            ):
                current += 1

            self.transactions = (
                self.transactions[:current]
                + [transaction]
                + self.transactions[current:]
            )
