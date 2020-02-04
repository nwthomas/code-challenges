const SparseArray = require("./sparseArray.js");

const utils = {
    smallNumberArray: [1, 5, 0, 0, 4, 0, 7],
    largeNumberArray: [5, 0, 0, 0, 9, 8, 0, 0, 1, 4, 0, 2, 3, 0, 6, 0]
};

describe("SparseArray", () => {
    describe("instantiates", () => {
        test("instantiates a new version of the SparseArray class correctly", () => {
            const result = new SparseArray([], 0);
            expect(result instanceof SparseArray).toBeTruthy();
        });

        test("returns an empty object if the first argument is not an array", () => {
            const result = new SparseArray("test", 0);
            expect(result).toEqual({});
        });

        test("returns an empty object if the second argument is not a number", () => {
            const result = new SparseArray([], "test");
            expect(result).toEqual({});
        });

        test("returns an empty object if the size argument is less than the array length", () => {
            const result = new SparseArray(utils.smallNumberArray, 0);
            expect(result).toEqual({});
        });

        test("instantiates with an array of numbers and only adds the non-zero values to \
        storage by index", () => {
            const s = new SparseArray([0, 0, 0, 3, 4, 0, 0, 2], 8);
            const result = s.storage;
            expect(result).toEqual({ 3: 3, 4: 4, 7: 2 });
        });
    });

    describe("set()", () => {
        test("sets a single value at a given index", () => {
            const s = new SparseArray(utils.smallNumberArray, 10);
            const initialResult = s.storage[0];
            expect(initialResult).toBe(1);
            s.set(0, 8);
            const afterResult = s.storage[0];
            expect(afterResult).toBe(8);
        });

        test("returns an empty object if the index argument is greater than the size of the array", () => {
            const s = new SparseArray(utils.largeNumberArray, 20);
            const result = s.set(21, 100);
            expect(result).toBeNull();
        });

        test("increases the size of the SparseArray if the index argument is greater than current length but shorter than max length", () => {
            const s = new SparseArray(utils.smallNumberArray, 20);
            s.set(8, 12);
            const result = s.currentLength;
            expect(result).toBe(8);
        });
    });
});
