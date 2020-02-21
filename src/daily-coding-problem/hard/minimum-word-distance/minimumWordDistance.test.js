const findMinimumWordDistance = require("./minimumWordDistance.js");

describe("Minimum Word Distance", () => {
    test("throws a new TypeError if the first argument is not a string", () => {
        const result = () => findMinimumWordDistance({}, "test", "test test");
        expect(result).toThrow(
            TypeError("The first argument must be a string")
        );
    });

    test("throw a new TypeError if the second argument is not a string", () => {
        const result = () => findMinimumWordDistance("test", {}, "test test");
        expect(result).toThrow(
            TypeError("The second argument must be a string")
        );
    });

    test("throws a new TypeError if the third argument is not a string", () => {
        const result = () => findMinimumWordDistance("test", "test", {});
        expect(result).toThrow(
            TypeError("The third argument must be a string")
        );
    });

    test("throws a new TypeError if the third argument is shorter than the first two plus a space", () => {
        const result = () => findMinimumWordDistance("test", "test", "test");
        expect(result).toThrow(
            Error(
                "The length of the third argument must be greater than the length of the first two arguments"
            )
        );
    });

    test("returns the correct number of words between two words at the beginning and end of a string", () => {
        const result = findMinimumWordDistance(
            "blue",
            "red",
            "blue orange green red"
        );
        expect(result).toBe(2);
    });

    test("returns the correct minimum number of words in a string with multiple solutions", () => {
        const result = findMinimumWordDistance(
            "blue",
            "red",
            "blue green blue green red red green blue"
        );
        expect(result).toBe(1);
    });

    test("resets the tracking number every time it encounters the starting word if it hasn't encountered the ending word", () => {
        const result = findMinimumWordDistance(
            "blue",
            "red",
            "blue blue blue blue blue red"
        );
        expect(result).toBe(0);
    });
});
