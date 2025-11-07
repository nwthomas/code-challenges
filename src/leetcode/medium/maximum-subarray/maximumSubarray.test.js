const { maxSubArray } = require("./maximumSubarray.js");

describe("maxSubArray", () => {

    test("returns the largest sum of a short array of numbers", () => {
        const result = maxSubArray([5,4,-1,7,8]);
        expect(result).toBe(23);
    });

    test("returns the largest sum of a medium array of numbers", () => {
        const result = maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]);
        expect(result).toBe(6);
    });
});