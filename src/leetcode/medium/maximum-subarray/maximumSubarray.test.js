const { maxSubArray } = require("./maximumSubarray.js");

describe("maxSubArray", () => {
    test("returns the value for an array of length 1", () => {
        const result = maxSubArray([10]);
        expect(result).toBe(10);
    });

    test("returns the value for a short array", () => {
        const result = maxSubArray([1, 4, 28, -100, 4, 40, 13]);
        expect(result).toBe(57);
    });

    test("returns the value for a long array", () => {
        const result = maxSubArray([
            1, 4, 28, -100, 4, 40, 13, 1000, -200, -400, 500, 3, -20, -300, 100,
        ]);
        expect(result).toBe(1057);
    });
});
