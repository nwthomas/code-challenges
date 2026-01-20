/*
https://prachub.com/interview-questions/implement-credit-ledger-with-out-of-order-timestamps
*/

const { heapPush, heapPop } = require("heapq");

const ACTIONS = {
    ADD_CREDIT: "add_credit",
    CHARGE_CREDIT: "charge_credit",
};

function compareExpirationTimestamps(a, b) {
    return a.expirationTimestamp < b.expirationTimestamp;
}

class Transaction {
    constructor(action, timestamp, amount, expirationTimestamp) {
        this.action = action;
        this.timestamp = timestamp;
        this.amount = amount;
        this.expirationTimestamp = expirationTimestamp || Infinity;
    }

    clone = () => {
        return new Transaction(
            this.action,
            this.timestamp,
            this.amount,
            this.expirationTimestamp,
        );
    };
}

class GPUCreditTracker {
    constructor() {
        this.transactions = [];
    }

    addCredit = (timestamp, expirationTimestamp, amount) => {
        const grantTransaction = new Transaction(
            ACTIONS.ADD_CREDIT,
            timestamp,
            amount,
            expirationTimestamp,
        );
        this._insertTransaction(grantTransaction);
    };

    chargeCredit = (timestamp, amount) => {
        const subtractTransaction = new Transaction(
            ACTIONS.CHARGE_CREDIT,
            timestamp,
            amount,
        );
        this._insertTransaction(subtractTransaction);
    };

    getBalance = (timestamp) => {
        const grantHeap = [];
        let current = 0;

        while (
            current < this.transactions.length &&
            this.transactions[current].timestamp <= timestamp
        ) {
            const currentTransaction = this.transactions[current].clone();

            while (
                grantHeap.length > 0 &&
                grantHeap[0].experationTimestamp < currentTransaction.timestamp
            ) {
                heapPop(grantHeap, compareExpirationTimestamps);
            }

            if (currentTransaction.action === ACTIONS.ADD_CREDIT) {
                heapPush(
                    grantHeap,
                    currentTransaction,
                    compareExpirationTimestamps,
                );
            } else {
                let totalSubtractRemaining = currentTransaction.amount;

                while (grantHeap.length > 0 && totalSubtractRemaining > 0) {
                    const currentGrantRemainingAmount = grantHeap[0].amount;
                    if (currentGrantRemainingAmount >= totalSubtractRemaining) {
                        grantHeap[0].amount -= totalSubtractRemaining;
                        totalSubtractRemaining = 0;
                    } else {
                        totalSubtractRemaining -= currentGrantRemainingAmount;
                        heapPop(grantHeap);
                    }
                }
            }

            current += 1;
        }

        let total = 0;
        while (grantHeap.length > 0) {
            const currentGrant = heapPop(
                grantHeap,
                compareExpirationTimestamps,
            );
            if (currentGrant.expirationTimestamp >= timestamp) {
                total += currentGrant.amount;
            }
        }
        return total;
    };

    _insertTransaction = (transaction) => {
        if (!this.transactions.length) {
            this.transactions.push(transaction);
        } else {
            let current = 0;

            while (
                current < this.transactions.length &&
                // Place add credits at beginning of timestamp
                ((transaction.action === ACTIONS.ADD_CREDIT &&
                    this.transactions[current].timestamp <
                        transaction.timestamp) ||
                    // Place charge credits at end of timestamp
                    (transaction.action === ACTIONS.CHARGE_CREDIT &&
                        this.transactions[current].timestamp <=
                            transaction.timestamp))
            ) {
                current++;
            }

            this.transactions = this.transactions
                .slice(0, current)
                .concat([transaction])
                .concat(this.transactions.slice(current));
        }
    };
}

module.exports = {
    GPUCreditTracker,
    Transaction,
};
