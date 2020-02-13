const findNearestLargerInteger = require("./nearestLargerNumber.js");

describe("findNearestLargerInteger()", () => {
    test("throws a new TypeError when the first argument is not an array", () => {
        const result = () => findNearestLargerInteger("test", 8);
        expect(result).toThrow(
            TypeError(
                "The first argument for findNearestLargerNumber must be an array of numbers"
            )
        );
    });

    test("throws a new TypeError when the second argument is not a number", () => {
        const result = () => findNearestLargerInteger([1, 2, 3, 4, 5], "test");
        expect(result).toThrow(
            TypeError(
                "The second argument for findNearestLargerNumber must be a number"
            )
        );
    });

    test("returns null when the length of the numberArray is 0", () => {
        const result = findNearestLargerInteger([], 0);
        expect(result).toBeNull();
    });

    test("returns null if the index is less than 0", () => {
        const result = findNearestLargerInteger([4, 3, 8], -1);
        expect(result).toBeNull();
    });

    test("returns null when the index is greater-or-equal-to the length of the numberArray", () => {
        const result = findNearestLargerInteger([4, 5, 3, 5], 4);
        expect(result).toBeNull();
    });

    test("returns the nearest larger integer index for a small array", () => {
        const result = findNearestLargerInteger([4, 3, 8, 2, 1], 1);
        expect(result).toBe(0);
    });

    test("returns the nearest larger integer index in a large array", () => {
        const result = findNearestLargerInteger(
            [6, 3, 1, 1, 9, 6, 3, 23, 34, 67, 8, 1, 4, 5],
            4
        );
        expect(result).toBe(7);
    });

    test("returns the nearest larger integer when it's the last index in the numberArray", () => {
        const result = findNearestLargerInteger([4, 6, 10, 8, 0, 11], 2);
        expect(result).toBe(5);
    });
});
