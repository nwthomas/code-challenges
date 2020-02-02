const SparseArray = require("./sparseArray.js");

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

        test("instantiates with an array of numbers and only adds the non-zero values to \
        storage by index", () => {
            const s = new SparseArray([0, 0, 0, 3, 4, 0, 0, 2], 8);
            const result = s.storage;
            expect(result).toEqual({ 3: 3, 4: 4, 7: 2 });
        });
    });

    describe("set()", () => {});
});
