from copy import deepcopy
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import List

from enum import Enum


class Action(Enum):
    GRANT = "grant"
    SUBTRACT = "subtract"


@dataclass
class Grant:
    """
    Marks a grant transaction at a given timestamp for a ceratin amount with a certain expiration
    timestamp.
    """

    action = Action.GRANT
    timestamp: int
    amount: int
    expiration_timestamp: int

    def __lt__(self, other_value) -> bool:
        """Compares two transactions. Required for heap comparisons."""
        return self.expiration_timestamp < other_value.expiration_timestamp


@dataclass
class Subtract:
    """
    Marks a subtract transaction at a given timestamp for a certain amount.
    """

    action = Action.SUBTRACT
    timestamp: int
    amount: int


class GPUCreditTracker:
    """
    Implements the ability to create GPU credit grants, subtract credits, and get the credit
    balance at a given point in time.
    """

    def __init__(self):
        self.transactions: List[Grant | Subtract] = []

    def create_grant(
        self, timestamp: int, expiration_timestamp: int, amount: int
    ) -> None:
        """Creates a grant for a credit balance increase."""
        transaction = Grant(timestamp, amount, expiration_timestamp)
        self.__insert_transaction(transaction)

    def subtract(self, timestamp: int, amount: int) -> None:
        """Subtracts credits from the current balance if possible."""
        transaction = Subtract(timestamp, amount)
        self.__insert_transaction(transaction)

    def get_balance(self, timestamp: int) -> int | None:
        """Returns the balance at a certain point in time."""
        has_gone_negative = False
        grant_heap: list[Grant] = []
        i = 0

        while (
            i < len(self.transactions) and self.transactions[i].timestamp <= timestamp
        ):
            current_transaction = deepcopy(self.transactions[i])

            # Clear out stale grants that have expired and can no longer be used
            while (
                grant_heap
                and grant_heap[0].expiration_timestamp < current_transaction.timestamp
            ):
                heappop(grant_heap)

            if isinstance(current_transaction, Grant):
                heappush(grant_heap, current_transaction)
            elif isinstance(current_transaction, Subtract):
                total_subtract_remaining = current_transaction.amount

                while grant_heap and total_subtract_remaining > 0:
                    current_grant_remaining_amount = grant_heap[0].amount

                    if current_grant_remaining_amount >= total_subtract_remaining:
                        grant_heap[0].amount -= total_subtract_remaining
                        total_subtract_remaining = 0
                    else:
                        total_subtract_remaining -= grant_heap[0].amount
                        heappop(grant_heap)

                # Any leftover balance at a timestamp means that the account is in a not recoverable
                # state and None should always be returned from this point forward. Exit immediately.
                if total_subtract_remaining > 0:
                    has_gone_negative = True
                    break

            i += 1

        # Calculate the remaining balance from the grant heap if not in unrecoverable state
        total = 0
        while not has_gone_negative and grant_heap:
            current_grant = heappop(grant_heap)

            if current_grant.expiration_timestamp > timestamp:
                total += current_grant.amount

        return total if not has_gone_negative else None

    def __insert_transaction(self, transaction: Grant | Subtract) -> None:
        """Inserts a new transaction into the list of transactions."""
        new_transaction: Grant | Subtract | None = transaction
        new_transactions_list: list[Grant | Subtract] = []

        for i, t in enumerate(self.transactions):
            if i == 0 and new_transaction and new_transaction.timestamp < t.timestamp:
                new_transactions_list.insert(0, new_transaction)
                new_transaction = None

            new_transactions_list.append(t)

            if (
                i + 1 < len(self.transactions)
                and new_transaction
                and (
                    t.timestamp
                    < new_transaction.timestamp
                    < self.transactions[i + 1].timestamp
                )
            ):
                new_transactions_list.append(new_transaction)
                new_transaction = None

        if new_transaction:
            new_transactions_list.append(new_transaction)

        self.transactions = new_transactions_list
