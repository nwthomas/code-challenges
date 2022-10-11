/*

Write a class called Spreadsheet that will write (put) and obtain (get) values from a table
like in Excel. You can assume that values accessed will exist, but we may want to create a
caching system in order to avoid multiple highly intensive computational actions.

*/

class Spreadsheet {
    constructor() {
        this.cells = {};
        this.cache = {};
        this.graph = {};
    }

    put(cell, value) {
        this._recursivelyClearCache(cell);
        this.graph[cell] = [];
        this.cells[cell] = value;
    }

    get(cell) {
        const value = this.cells[cell];
        const splitCells = value.split("=").join("").split("+");
        let additionValue = 0;

        for (let cellKey of splitCells) {
            const convertedCellKey = parseInt(cellKey, 10);

            if (isNaN(convertedCellKey)) {
                const recursivelyComputedValue = this.get(cellKey);
                this._addGraphDependency(cell, cellKey);

                additionValue += recursivelyComputedValue;
            } else {
                additionValue += convertedCellKey;
            }
        }

        this.cache[cell] = additionValue;

        return this.cache[cell];
    }

    _addGraphDependency(cell, dep) {
        if (!this.graph[cell]) {
            this.graph[cell] = [];
        }

        this.graph[cell].push(dep);
    }

    _recursivelyClearCache(key) {
        delete this.cache[key];

        if (!this.graph[key]) {
            this.graph[key] = [];
        }

        for (let dep of this.graph[key]) {
            this._recursivelyClearCache(dep);
        }
    }
}

module.exports = Spreadsheet;
