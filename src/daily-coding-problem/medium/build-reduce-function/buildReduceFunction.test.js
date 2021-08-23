const reduce = require("./buildReduceFunction.js");

const largeNumArray = [
    7, 1, 4, 7, 234, 56, 43, 91, 687, 1, 4, 6, 8, 2, 4, 5, 90, 45,
];
const smallNumArray = [1, 4, 7, 10, 9, 45];

describe("reduce", () => {
    test("throw error when first argument is not an array", () => {
        const result = () => reduce({}, () => "test", "");
        expect(result).toThrow(
            Error("The first argument of reduce must be an array."),
        );
    });

    test("throw error when second argument is not a function", () => {
        const result = () => reduce(smallNumArray, {}, 0);
        expect(result).toThrow(
            Error("The second argument of reduce must be a function."),
        );
    });

    test("returns correct sum for reduce array with small array of numbers", () => {
        const add = (accum, nextNum) => accum + nextNum;
        const result = reduce(smallNumArray, add, 0);
        expect(result).toBe(76);
    });

    test("returns correct product for reduce array with large array of numbers", () => {
        const multiply = (accum, nextNum) => accum * nextNum;
        const result = reduce(largeNumArray, multiply, 1);
        expect(result).toBe(214754752736649200000);
    });

    test("works with other data types", () => {
        const stringArray = ["this", "is", "a", "test"];
        const combineStrings = (accum, nextString, i, arr) => {
            return i !== arr.length - 1
                ? accum + nextString + " "
                : accum + nextString;
        };
        const result = reduce(stringArray, combineStrings, "");
        expect(result).toBe("this is a test");
    });
});
