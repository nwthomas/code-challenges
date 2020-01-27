const findMaxSumSubarray = require("./maximumSumSubarray.js");

describe("findMaxSumSubarray()", () => {
    test("returns null if the argument passed in is not an array", () => {
        const result = findMaxSumSubarray("test");
        expect(result).toBeNull();
    });

    test("returns 0 if the array has no length", () => {
        const result = findMaxSumSubarray([]);
        expect(result).toBe(0);
    });

    test("returns 0 if all the numbers in the array are negative", () => {
        const result = findMaxSumSubarray([-9, -4, -3, -2, -1, -10, -1234]);
        expect(result).toBe(0);
    });

    test("returns the correct maximum sum subarray of a small array of numbers", () => {
        // the maximum should be the sum of 7, 3, and 5
        const result = findMaxSumSubarray([7, 3, 5, -10, -4, 5, 0, 4]);
        expect(result).toBe(15);
    });

    test("returns the correct maximum sum subarray of a large array of numbers", () => {
        // the maximum should be the sum of 123, 6, 8, and 546
        const result = findMaxSumSubarray([
            4,
            6,
            -1,
            -4,
            -15,
            345,
            3,
            -13,
            -5678,
            -123,
            123,
            6,
            8,
            546,
            0
        ]);
        expect(result).toBe(683);
    });
});
