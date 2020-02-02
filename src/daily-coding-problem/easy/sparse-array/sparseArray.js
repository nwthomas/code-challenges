/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    
    set(i, val): updates index at i with val.
    
    get(i): gets the value at index i.
*/

function SparseArray(arr, size) {
    /**
     * Constructor function for SparseArray class. Instantiates a new SparseArray of a specific
     * size and stores anh data accordingly
     *
     * @param {array} arr The original array to be stored in the SparseArray
     *
     * @param {number} size The size of the list
     */

    if (!Array.isArray(arr) || typeof size !== "number") {
        return null;
    }

    this.size = size;
    this.storage = {};

    arr.forEach((val, i) => {
        if (val !== 0) {
            this.storage[i] = val;
        }
    });

    return arr;
}

SparseArray.prototype.set = function set(index, val) {
    /**
     * Stores a value with the associated index
     *
     * @param {number} index The index of of the value to be stored
     */

    this.storage[index] = val;

    if (index >= this.size) {
        this.size++;
    }
};

SparseArray.prototype.get = function get(index) {
    /**
     * Returns the value at index of i if that value is contained in the object or else the
     * number 0
     *
     * @param {number} i The index of the value to be retrieved
     */

    return this.storage[index] ? this.storage[index] : 0;
};

SparseArray.prototype.retrieveArray = function retrieveArray() {
    /**
     * Returns the full array stored inside SparseArray
     *
     * @returns {array} The array stored inside SparseArray
     */

    const arr = [];

    for (let i = 0; i < this.size; i++) {
        if (this.storage[i]) {
            arr.push(this.storage[i]);
        } else {
            arr.push(0);
        }
    }

    return arr;
};

SparseArray.prototype.push = function push(val) {
    /**
     * Adds a new value to the end of the SparseArray
     *
     * @param {any} val The value to be added to the end of the SparseArray
     */

    this.storage[this.size] = val;
    this.size++;
};

SparseArray.prototype.pop = function pop() {
    /**
     * Pops the value off the end of the SparseArray
     *
     * @returns {any} The value at the end of the SparseArray
     */

    this.size--;

    if (this.storage[this.size - 1]) {
        const val = this.storage[this.size - 1];
        delete this.storage[this.size - 1];
        return val;
    } else {
        return 0;
    }
};

SparseArray.prototype.shift = function shift() {
    /**
     * Shifts the value from the front of the SparseArray
     *
     * @returns {any} The value from the front of the SparseArray
     */

    let val = null;

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

    this.size--;

    return val;
};

SparseArray.prototype.unshift = function unshift(val) {
    /**
     * Adds a new value to the front of the SparseArray
     *
     * @param {any} val The value to be added to the front of the SparseArray
     */

    this.size++;

    for (let i = this.size; i >= 1; i++) {
        if (this.storage[i - 1]) {
            this.storage[i] = this.storage[i - 1];
            delete this.storage[i - 1];
        }
    }

    this.storage[0] = val;
};

module.exports = SparseArray;
