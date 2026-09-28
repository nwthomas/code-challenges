/*
https://prachub.com/interview-questions/implement-credit-ledger-with-out-of-order-timestamps
*/

import { heapPush, heapPop } from "heapq";

type Action = "add_credit" | "charge_credit";

const ACTION = {
    ADD_CREDIT: "add_credit",
    CHARGE_CREDIT: "charge_credit",
} as const;

function comparator(a: Transaction, b: Transaction) {
    return a.expirationTimestamp < b.expirationTimestamp;
}

class Transaction {
    action: Action;
    amount: number;
    timestamp: number;
    expirationTimestamp: number;

    constructor(
        action: Action,
        amount: number,
        timestamp: number,
        expirationTimestamp: number = Infinity,
    ) {
        this.action = action;
        this.amount = amount;
        this.timestamp = timestamp;
        this.expirationTimestamp = expirationTimestamp;
    }

    clone = () => {
        return new Transaction(
            this.action,
            this.amount,
            this.timestamp,
            this.expirationTimestamp,
        );
    };
}

class GPUCreditTracker {
    transactions: Transaction[];

    constructor() {
        this.transactions = [];
    }

    _insertTransaction = (transaction: Transaction) => {
        if (this.transactions.length === 0) {
            this.transactions.push(transaction);
        } else {
            let index = 0;

            while (
                index < this.transactions.length &&
                ((transaction.action === ACTION.ADD_CREDIT &&
                    this.transactions[index].timestamp <
                        transaction.timestamp) ||
                    (transaction.action === ACTION.CHARGE_CREDIT &&
                        this.transactions[index].timestamp <=
                            transaction.timestamp))
            ) {
                index++;
            }

            this.transactions = this.transactions
                .slice(0, index)
                .concat([transaction])
                .concat(this.transactions.slice(index));
        }
    };

    addCredit = (
        timestamp: number,
        expirationTimestamp: number | undefined,
        amount: number,
    ) => {
        this._insertTransaction(
            new Transaction(
                ACTION.ADD_CREDIT,
                amount,
                timestamp,
                expirationTimestamp,
            ),
        );
    };

    chargeCredit = (timestamp: number, amount: number) => {
        this._insertTransaction(
            new Transaction(ACTION.CHARGE_CREDIT, amount, timestamp),
        );
    };

    getBalance = (timestamp: number) => {
        const minHeap: Transaction[] = [];
        let index = 0;

        while (
            index < this.transactions.length &&
            this.transactions[index].timestamp <= timestamp
        ) {
            const current = this.transactions[index].clone();

            while (
                minHeap.length > 0 &&
                minHeap[0].expirationTimestamp < current.timestamp
            ) {
                heapPop(minHeap, { comparator });
            }

            if (current.action === ACTION.ADD_CREDIT) {
                heapPush(minHeap, current, { comparator });
            } else {
                let subtractRemaining = current.amount;

                while (minHeap.length > 0 && subtractRemaining > 0) {
                    if (minHeap[0].amount >= subtractRemaining) {
                        minHeap[0].amount -= subtractRemaining;
                        subtractRemaining = 0;
                    } else {
                        subtractRemaining -= minHeap[0].amount;
                        heapPop(minHeap, { comparator });
                    }
                }
            }

            index += 1;
        }

        let total = 0;
        while (minHeap.length > 0) {
            const current = heapPop(minHeap, { comparator })!;
            if (current.expirationTimestamp >= timestamp) {
                total += current.amount;
            }
        }

        return total;
    };
}

export { GPUCreditTracker, Transaction };
