/*
https://prachub.com/interview-questions/implement-credit-ledger-with-out-of-order-timestamps
*/

const { heapPush, heapPop } = require("heapq");

const ACTION = {
    ADD_CREDIT: "add_credit",
    CHARGE_CREDIT: "charge_credit",
};

function comparator(a, b) {
    return a.expirationTimestamp < b.expirationTimestamp;
}

class Transaction {
    constructor(action, amount, timestamp, expirationTimestamp = Infinity) {
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
    constructor() {
        this.transactions = [];
    }

    _insertTransaction = (transaction) => {
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

    addCredit = (timestamp, expirationTimestamp, amount) => {
        this._insertTransaction(
            new Transaction(
                ACTION.ADD_CREDIT,
                amount,
                timestamp,
                expirationTimestamp,
            ),
        );
    };

    chargeCredit = (timestamp, amount) => {
        this._insertTransaction(
            new Transaction(ACTION.CHARGE_CREDIT, amount, timestamp),
        );
    };

    getBalance = (timestamp) => {
        const minHeap = [];
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
            const current = heapPop(minHeap, { comparator });
            if (current.expirationTimestamp >= timestamp) {
                total += current.amount;
            }
        }

        return total;
    };
}

module.exports = {
    GPUCreditTracker,
    Transaction,
};
