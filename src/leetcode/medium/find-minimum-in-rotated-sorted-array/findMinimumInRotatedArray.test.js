const { findMin } = require("./findMinimumInRotatedArray.js");

describe(findMin.name, () => {
    test("returns min with array length one", () => {
        const result = findMin([777]);
        expect(result).toBe(777);
    });

    test("returns min with array length two", () => {
        const result = findMin([4, 17]);
        expect(result).toBe(4);
    });

    test("returns min with rotated array", () => {
        const result = findMin([6, 7, 8, 9, 0, 1, 2, 3, 4, 5]);
        expect(result).toBe(0);
    });

    test("returns min with non-rotated array", () => {
        const result = findMin([
            4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 50, 60, 10000000,
        ]);
        expect(result).toBe(4);
    });
});
