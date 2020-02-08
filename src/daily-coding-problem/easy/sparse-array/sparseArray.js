/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    
    set(i, val): updates index at i with val.
    
    get(i): gets the value at index i.
*/

function SparseArray(arr = null, size = null) {
    /**
     * Constructor function for SparseArray class. Instantiates a new SparseArray of a specific
     * size and stores the data accordingly
     *
     * @param {array} arr The original array to be stored in the SparseArray
     *
     * @param {number} size The size of the list
     *
     * @returns {(SparseArray|object)} Returns a new SparseArray or an empty object if given the
     * wrong arguments
     */

    if (!Array.isArray(arr) || typeof size !== "number" || arr.length > size) {
        return {};
    }

    this.currentLength = 0;
    this.size = size;
    this.storage = {};

    arr.forEach((val, i) => {
        this.currentLength++;

        if (val !== 0) {
            this.storage[i] = val;
        }
    });
}

SparseArray.prototype.set = function set(index, val) {
    /**
     * Stores a value with the associated index
     *
     * @param {number} index The index of of the value to be stored
     *
     * @returns {(any|null)} Returns the value if added successfully, or otherwise null
     */

    if (index > this.size - 1 || index > this.currentLength + 1) {
        return null;
    }

    if (index > this.currentLength && index < this.size) {
        this.currentLength++;
    }

    this.storage[index] = val;

    return val;
};

SparseArray.prototype.get = function get(index) {
    /**
     * Returns the value at index of i if that value is contained in the object or else the
     * number 0
     *
     * @param {number} i The index of the value to be retrieved
     *
     * @returns {(any|null)} Returns the value stored at the specified index, the number 0,
     * or null
     */

    if (index > this.size - 1 || index > this.currentLength) {
        return null;
    }

    return this.storage[index] ? this.storage[index] : 0;
};

SparseArray.prototype.retrieveArray = function retrieveArray() {
    /**
     * Returns the full array stored inside SparseArray
     *
     * @returns {array} The array of values stored inside SparseArray
     */

    if (!this.currentLength) {
        return [];
    }

    const arr = [];

    for (let i = 0; i < this.currentLength; i++) {
        if (this.storage[i]) {
            arr.push(this.storage[i]);
        } else {
            arr.push(0);
        }
    }

    return arr;
};

SparseArray.prototype.pushValue = function pushValue(val) {
    /**
     * Adds a new value to the end of the SparseArray
     *
     * @param {any} val The value to be added to the end of the SparseArray
     *
     * @returns {(any|null)} Returns the value that has been added to the SparseArray or else null
     */

    if (this.currentLength >= this.size) {
        return null;
    }

    this.currentLength++;
    this.storage[this.currentLength - 1] = val;

    return val;
};

SparseArray.prototype.popValue = function popValue() {
    /**
     * Pops the value off the end of the SparseArray
     *
     * @returns {any} The value at the end of the SparseArray
     */

    this.currentLength--;

    if (this.storage[this.currentLength]) {
        const val = this.storage[this.currentLength];
        delete this.storage[this.currentLength];
        return val;
    } else {
        return 0;
    }
};

SparseArray.prototype.shiftValue = function shiftValue() {
    /**
     * Shifts the value from the front of the SparseArray
     *
     * @returns {(any|null)} The value from the front of the SparseArray or else null
     */

    let val = null;

    if (this.currentLength === 0) {
        return val;
    }

    if (this.storage[0]) {
        val = this.storage[0];
        delete this.storage[0];
    } else {
        val = 0;
    }

    for (let i = 0; i < this.size; i++) {
        if (this.storage[i + 1]) {
            const val = this.storage[i + 1];
            delete this.storage[i + 1];
            this.storage[i] = val;
        }
    }

    this.currentLength--;

    return val;
};

SparseArray.prototype.unshiftValue = function unshiftValue(val) {
    /**
     * Adds a new value to the front of the SparseArray
     *
     * @param {any} val The value to be added to the front of the SparseArray
     *
     * @returns {(any|null)} Returns the new value added to the front of the SparseArray or
     * else null
     */

    if (this.currentLength + 1 > this.size) {
        return null;
    }

    this.currentLength++;

    for (let i = this.size - 1; i > 0; i--) {
        if (this.storage[i - 1]) {
            this.storage[i] = this.storage[i - 1];
            delete this.storage[i - 1];
        }
    }

    this.storage[0] = val;

    return val;
};

SparseArray.prototype.length = function length() {
    /**
     * Returns the current length of the SparseArray
     *
     * @returns {number} Returns the length of the SparseArray
     */

    return this.currentLength;
};

module.exports = SparseArray;
