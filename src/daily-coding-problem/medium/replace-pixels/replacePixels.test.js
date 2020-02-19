const { replacePixels, deepCopy } = require("./replacePixels.js");

describe("deepCopy()", () => {
    test("throws a new TypeError when the argument is not an array", () => {
        const result = () => deepCopy("test");
        expect(result).toThrow(
            TypeError("The argument of deepCopy must be an array")
        );
    });

    test("returns an identical version of the array of values passed as an argument", () => {
        const result = deepCopy([1, 4, 5, 2, 3]);
        expect(result).toEqual([1, 4, 5, 2, 3]);
    });

    test("handles sub-arrays nested inside the array to be copied", () => {
        const result = deepCopy([1, 2, [3, 6, 7, 9], 4, [[[5, 6]]]]);
        expect(result).toEqual([1, 2, [3, 6, 7, 9], 4, [[[5, 6]]]]);
    });
});

describe("replacePixels()", () => {
    // finish
});
