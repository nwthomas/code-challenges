/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
*/

class Implement2DIterator {
    constructor(_2DArray = []) {
        this._array = _2DArray;
        this._x = 0;
        this._y = 0;
        this._nextValue = null;

        if (
            Array.isArray(this._array) &&
            this._array.length &&
            this._y < this._array[this._x].length
        ) {
            this._nextValue = this._array[this._x][this._y];
        }
    }

    next() {
        /**
         * Returns the next item in the 2D Array if it exists
         *
         * @returns {(any|ReferenceError)} Returns the value if it exists or else a ReferenceError
         */
        let temp = this._nextValue;
        if (this._nextValue) {
            this._nextValue = null;
            return temp;
        } else if (this.hasNext()) {
            temp = this._nextValue;
            this._nextValue = null;
            return temp;
        } else {
            if (
                this._x >= this._array.length ||
                this._y >= this._array[this._x].length
            ) {
                throw new ReferenceError(
                    `The (x, y) indices of (${this._x}, ${this._y}) are not valid`
                );
            }
        }
    }

    hasNext() {
        /**
         * Determines whether or not there is another iterable item insdie the 2D array
         *
         * @returns {boolean} Returns true if there is a next value or else false
         */
        if (this._nextValue) {
            return true;
        } else {
            this._y++;
            while (true) {
                if (
                    this._x < this._array.length &&
                    this._y < this._array[this._x].length
                ) {
                    this._nextValue = this._array[this._x][this._y];
                    return true;
                } else if (this._x < this._array.length - 1) {
                    this._x++;
                    this._y = 0;
                } else {
                    return false;
                }
            }
        }
    }
}

module.exports = Implement2DIterator;
