const findSingleNumbers = require("./findSingleNumbers.js");

describe("findSingleNumbers()", () => {
    test("returns an empty array if the argument is less than length of 2", () => {
        const result = findSingleNumbers([1]);
        expect(result).toEqual([]);
    });

    test("returns an empty array if the argument is not of type array", () => {
        const result = findSingleNumbers("test");
        expect(result).toEqual([]);
    });

    test("returns an empty array if there are less than 2 equal numbers in the number array", () => {
        const result = findSingleNumbers([0, 3, 8, 2, 9, 0, 3, 8, 2]);
        expect(result).toEqual([]);
    });

    test("returns an empty array if there are mroe than 2 unique numbers in the number array", () => {
        const result = findSingleNumbers([0, 3, 4, 5, 8, 9]);
        expect(result).toEqual([]);
    });

    test("returns the two unique numbers in a number array that otherwise contains duplictes", () => {
        const result = findSingleNumbers([0, 3, 5, 2, 9, 3, 2, 9]);
        expect(result).toEqual([0, 5]);
    });
});
