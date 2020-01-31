/*
Good morning! Here's your coding interview problem for today.

This question was asked by Riot Games.

Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:

record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)

Follow-up: What if our system has limited memory?
*/

class HitCounter {
    constructor() {
        this.hitCounter = {};
        this.totalHits = 0;
    }

    record(timestamp = null) {
        if (
            typeof timestamp !== "string" &&
            typeof parseInt(timestamp) !== "number"
        ) {
            return null;
        } else {
            this.hitCounter[timestamp]
                ? this.hitCounter[timestamp]++
                : (this.hitCounter[timestamp] = 1);
            this.totalHits++;
            return { timestamp: this.hitCounter[timestamp] };
        }
    }

    range(lower = null, upper = null) {
        if (!lower || !upper) {
            return 0;
        }
        let total = 0;
        const _lower = parseInt(lower);
        const _upper = parseInt(upper);
        Object.entries(this.hitCounter).forEach(entry => {
            const key = parseInt(entry[0]);
            const value = entry[1];
            if (key >= _lower && key <= _upper) {
                total += value;
            }
        });
        return total;
    }

    total() {
        return this.totalHits;
    }
}

module.exports = HitCounter;
