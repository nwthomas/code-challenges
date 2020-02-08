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
        test("returns null if the index argument is greater than the size of the array", () => {
            const s = new SparseArray(utils.largeNumberArray, 20);
            const result = s.set(21, 100);
            expect(result).toBeNull();
        });

        test("returns null if the index argument is greater than + 1 the currentLength of the SparseArray", () => {
            const s = new SparseArray(utils.smallNumberArray, 1000);
            const result = s.set(100, 100);
            expect(result).toBeNull();
        });

        test("sets a single value at a given index", () => {
            const s = new SparseArray(utils.smallNumberArray, 10);
            const initialResult = s.storage[0];
            expect(initialResult).toBe(1);
            s.set(0, 8);
            const afterResult = s.storage[0];
            expect(afterResult).toBe(8);
        });

        test("increases the size of the SparseArray if the index argument is greater than current length but shorter than max length", () => {
            const s = new SparseArray(utils.smallNumberArray, 20);
            s.set(8, 12);
            const result = s.currentLength;
            expect(result).toBe(8);
        });

        test("increases the currentLength of the SparseArray when new items are added", () => {
            const s = new SparseArray(utils.smallNumberArray, 1000);
            const result = s.currentLength;
            expect(result).toBe(7);
        });

        test("returns the value set at the specified index if the value is added successfully", () => {
            const s = new SparseArray([], 1000);
            const result = s.set(0, 100);
            expect(result).toBe(100);
        });
    });

    describe("get()", () => {
        test("returns null if the index is greater than currentLength", () => {
            const s = new SparseArray(utils.largeNumberArray, 1000);
            const result = s.get(100);
            expect(result).toBeNull();
        });

        test("returns null if the index is greater than the size of the SparseArray", () => {
            const s = new SparseArray([], 100);
            const result = s.get(101);
            expect(result).toBeNull();
        });

        test("returns 0 if there is not value contained in SparseArray.storage", () => {
            const s = new SparseArray(utils.smallNumberArray, 100);
            const storageResult = s.storage[2];
            const zeroResult = s.get(2);
            expect(storageResult).toBeUndefined();
            expect(zeroResult).toBe(0);
        });

        test("returns the non-zero value if it's stored in SparseArray.storage", () => {
            const s = new SparseArray(utils.smallNumberArray, 100);
            const result = s.get(1);
            expect(result).toBe(5);
        });
    });

    describe("retrieveArray()", () => {
        test("returns the entire array passed into the SparseArray constructor", () => {
            const s = new SparseArray(utils.smallNumberArray, 100);
            const result = s.retrieveArray();
            expect(result).toEqual(utils.smallNumberArray);
        });

        test("returns an empty array if the SparseArray is empty", () => {
            const s = new SparseArray([], 1);
            const result = s.retrieveArray();
            expect(result).toEqual([]);
        });
    });

    describe("pushValue()", () => {
        test("returns null if the currentLength is greater than the size of the SparseArray", () => {
            const s = new SparseArray(utils.smallNumberArray, 8);
            s.pushValue(100);
            const result = s.pushValue(101);
            expect(result).toBeNull();
        });

        test("adds a value to the end of the SparseArray", () => {
            const s = new SparseArray(utils.smallNumberArray, 100);
            s.pushValue(6);
            const arr = s.retrieveArray();
            const result = arr[arr.length - 1];
            expect(result).toBe(6);
        });
    });

    describe("popValue()", () => {
        test("returns the value stored at the last index of the SparseArray", () => {
            const s = new SparseArray(utils.smallNumberArray, 100);
            const result = s.popValue();
            expect(result).toBe(7);
        });

        test("decreases the currentLength by 1", () => {
            const s = new SparseArray(utils.smallNumberArray, 100);
            const prevLength = s.currentLength;
            s.popValue();
            const resultLength = s.currentLength;
            expect(prevLength).toBe(7);
            expect(resultLength).toBe(6);
        });

        test("returns 0 if that value is the SparseArray value", () => {
            const s = new SparseArray([0, 3, 4, 0], 10);
            const result = s.popValue();
            expect(result).toBe(0);
        });
    });

    describe("shiftValue()", () => {
        test("returns null if the currentLength of the SparseArray is 0", () => {
            const s = new SparseArray([], 1);
            const result = s.shiftValue();
            expect(result).toBeNull();
        });

        test("returns the value from the front of the SparseArray", () => {
            const s = new SparseArray([1, 0, 0, 7], 10);
            const result = s.shiftValue();
            expect(result).toBe(1);
        });

        test("shifts the index of all other values in the SparseArray down by 1", () => {
            const s = new SparseArray([1, 8, 0, 0], 10);
            s.shiftValue();
            const result = s.storage[0]; //
            expect(result).toBe(8);
        });
    });

    describe("unshiftValue()", () => {
        test("returns null if the currentLength of the SparseArray will be greater than the determined size", () => {
            const s = new SparseArray([0, 1, 8, 9, 1], 5);
            const result = s.unshiftValue(8);
            expect(result).toBeNull();
        });

        test("returns the value stored at the front of the SparseArray", () => {
            const s = new SparseArray([0, 4, 5, 0, 0], 10);
            const result = s.unshiftValue(7);
            expect(result).toBe(7);
        });

        test("moves all values up by one index in the SparseArray", () => {
            const oldArr = [0, 4, 6, 8, 0, 0, 0, 2, 3];
            const s = new SparseArray(oldArr, 100);
            s.unshiftValue(10);
            const newArr = [10, ...oldArr];
            for (let i = 0; i < newArr.length; i++) {
                expect(s.get(i)).toBe(newArr[i]);
            }
        });
    });

    describe("length()", () => {
        test("returns 0 if no values have been added to the SparseArray", () => {
            const s = new SparseArray([], 10);
            const result = s.length();
            expect(result).toBe(0);
        });

        test("returns the current length of the SparseArray", () => {
            const s = new SparseArray(utils.largeNumberArray, 100);
            const result = s.length();
            expect(result).toBe(16);
        });
    });
});
