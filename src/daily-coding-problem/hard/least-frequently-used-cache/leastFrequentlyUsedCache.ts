/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Implement an LFU (Least Frequently Used) cache. It should be able to be initialized with a cache size n, and contain the following methods:

set(key, value): sets key to value. If there are already n items in the cache and we are adding a new item, then it should also remove the least frequently used item. If there is a tie, then the least recently used key should be removed.

get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.

*/

class Node {
    _value: [string, string | number];
    _previous: Node | null;
    _next: Node | null;

    constructor(value: [string, string | number]) {
        /**
         * Constructor function that instantiates a new Node
         *
         * @param {any} _value - Stores any value passed in as the initial Node value
         * @param {Node} _previous - Stores a reference to the previous Node in the cache
         * @param {Node} _next - Stores a reference to the next Node in the cache
         */
        this._value = value;
        this._previous = null;
        this._next = null;
    }
    delete() {
        /**
         * Deletes the references to this node from the _previous and _next Nodes
         * and allows garbage collection to clean it up
         *
         * It returns the _value of the Node
         */
        if (this._previous) {
            this._previous._next = this._next;
        }
        if (this._next) {
            this._next._previous = this._previous;
        }
        return this._value;
    }
}

class LeastFrequentlyUsedCache {
    declare _cache: Record<string, Node>;
    declare _head: Node | null;
    declare _tail: Node | null;
    declare _length: number;
    declare _cacheSize: number;

    constructor(cacheSize: number) {
        /**
         * Constuctor function that instantiates a new LFU cache
         *
         * @param {object} _cache - An object/hashmap reference for O(1) Node lookup time
         * @param {Node} _head - Stores a reference to the head Node of the LFU cache
         * @param {Node} _tail - Stores a reference to the tail Node of the LFU cache
         * @param {number} _length - Provides a conventient, up-to-date number value for
         * the length of the LFU cache
         * @param {number} _cacheSize - References the initial parameter cacheSize passed
         * in when the LFU cache was instantiated
         */
        if (cacheSize < 1 || typeof cacheSize !== "number") {
            return;
        }
        this._cache = {};
        this._head = null;
        this._tail = null;
        this._length = 0;
        this._cacheSize = cacheSize;
    }
    set(key: string, value: string | number) {
        /**
         * This method runs in O(1) time, sets the key and value into the
         * LFU cache, and returns the index of the newly-set key-value
         * pair
         */
        const stringKey = `${key}`;
        if (!this._head) {
            const node = new Node([stringKey, value]);
            this._head = node;
            this._tail = node;
            this._cache[stringKey] = node;
            this._length++;
        } else if (this._cache[stringKey]) {
            if (this._length === 1) {
                return;
            }
            let newTail;
            if (this._tail === this._cache[stringKey]) {
                newTail = this._tail._previous;
            }
            const oldNode = this._cache[stringKey].delete();
            const newNode = new Node([stringKey, value]);
            this._cache[stringKey] = newNode;
            this._head._previous = newNode;
            newNode._next = this._head;
            this._head = newNode;
            if (newTail) {
                this._tail = newTail;
            }
        } else {
            const node = new Node([stringKey, value]);
            node._next = this._head;
            this._head._previous = node;
            this._head = node;
            this._cache[stringKey] = node;
            this._length++;
        }
        if (this._length > this._cacheSize && this._tail) {
            const newTailNode = this._tail._previous;
            const oldNodeKey = this._tail._value[0];
            this._tail.delete();
            this._tail = newTailNode;
            delete this._cache[oldNodeKey];
            this._length--;
        }
    }

    get(key: string) {
        /**
         * This method runs in O(1) time and returns the value
         * associated with the key passed in as a parameter
         */
        const stringKey = `${key}`;
        const value = this._cache[stringKey] && this._cache[stringKey]._value;
        if (value) {
            return value;
        }
        return null;
    }

    length() {
        /**
         * This method runs in O(1) time to access the length of the LRU cache
         *
         * It returns the number value of the length of the cache
         */
        return this._length;
    }
}

export { LeastFrequentlyUsedCache, Node };
