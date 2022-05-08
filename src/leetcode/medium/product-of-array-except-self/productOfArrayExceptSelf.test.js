const { productExceptSelf } = require("./productOfArrayExceptSelf.js");

describe("productExceptSelf", () => {
    test("returns reversed array for array length 2", () => {
        const result = productExceptSelf([0, 1]);
        expect(result).toEqual([1, 0]);
    });

    test("returns array of 1 item", () => {
        const result = productExceptSelf([9]);
        expect(result).toEqual([9]);
    });

    test("returns empty array", () => {
        const result = productExceptSelf([]);
        expect(result).toEqual([]);
    });

    test("returns complete array where every index is total product of all other indices", () => {
        const result = productExceptSelf([1, 2, 3, 4, 5, 6, 7, 8, 9]);
        expect(result).toEqual([
            362880, 181440, 120960, 90720, 72576, 60480, 51840, 45360, 40320,
        ]);
    });
});
