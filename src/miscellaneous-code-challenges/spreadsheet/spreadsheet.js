/*

Write a class called Spreadsheet that will write (put) and obtain (get) values from a table
like in Excel. You can assume that values accessed will exist, but we may want to create a
caching system in order to avoid multiple highly intensive computational actions.

*/

class Spreadsheet {
    constructor() {
        this.cache = {};
        this.cells = {};
        this.graph = {};
    }

    put = (key, value) => {
        this.cells[key] = value;
        this._recursivelyClearCache(key);
        this.graph[key] = [];
    };

    get = (key) => {
        if (this.cache[key]) {
            return this.cache[key];
        }

        const value = this.cells[key];
        const valuesArray = value.split("=").join("").split("+");

        let total = 0;

        for (const currentValue of valuesArray) {
            const convertedValue = parseInt(currentValue, 10);

            if (isNaN(convertedValue)) {
                total += this.get(currentValue);
                this._addGraphDependency(currentValue, key);
            } else {
                total += convertedValue;
            }
        }

        this.cache[key] = total;

        return total;
    };

    _recursivelyClearCache = (key) => {
        delete this.cache[key];

        if (!this.graph[key]) {
            this.graph[key] = [];
        }

        this.graph[key].forEach((dep) => {
            this._recursivelyClearCache(dep);
        });
    };

    _addGraphDependency = (child, parent) => {
        this.graph[child] = this.graph[child] || [];

        this.graph[child].push(parent);
    };
}

module.exports = Spreadsheet;
