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
});
