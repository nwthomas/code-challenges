const findSmallerToRightInArray = require("./smallerToRight.js");

describe("findSmallerToRightInArray()", () => {
    test("throws a TypeError if the input argument is not an array", () => {
        const result = () => findSmallerToRightInArray("test");
        expect(result).toThrow(TypeError("The argument must be an array"));
    });

    test("returns an empty array if the argument is an empty array", () => {
        const result = findSmallerToRightInArray([]);
        expect(result).toEqual([]);
    });

    test("returns a list of number that equal the smaller numbers to their right in a short array", () => {
        const result = findSmallerToRightInArray([1, 4, 2, 5]);
        expect(result).toEqual([0, 1, 0, 0]);
    });

    test("returns a list of number that equal the smaller numbers to their right", () => {
        const result = findSmallerToRightInArray([
            4,
            10,
            3,
            7,
            8,
            1,
            2,
            3,
            4,
            5
        ]);
        expect(result).toEqual([4, 8, 2, 5, 5, 0, 0, 0, 0, 0]);
    });

    test("handles a series of duplicates of the same lesser number", () => {
        const result = findSmallerToRightInArray([10, 8, 8, 8, 8, 8, 8, 8]);
        expect(result).toEqual([7, 0, 0, 0, 0, 0, 0, 0]);
    });

    test("throws a new TypeError if one of the values of the argument array is not a number", () => {
        const result = () => findSmallerToRightInArray([1, 2, 3, "test"]);
        expect(result).toThrow(
            TypeError("The array must only contain numbers")
        );
    });
});
