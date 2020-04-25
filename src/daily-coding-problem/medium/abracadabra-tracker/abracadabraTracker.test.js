const findPatternStartingIndices = require("./abracadabraTracker.js");

describe("Abracadabra Tracker", () => {
    test("throws a TypeError if the first argument is not a string", () => {
        const result = () => findPatternStartingIndices({}, "abcdefg");
        expect(result).toThrow(
            TypeError(
                "The arguments for findPatternStartingIndices must be strings."
            )
        );
    });

    test("throws a TypeError if the second argument is not a string", () => {
        const result = () => findPatternStartingIndices("abc", {});
        expect(result).toThrow(
            TypeError(
                "The arguments for findPatternStartingIndices must be strings."
            )
        );
    });

    test("returns a starting index for a pattern if it is contained inside the string", () => {
        const result = findPatternStartingIndices("abc", "uiyoiuabcoi7tugh");
        expect(result).toEqual([6]);
    });
});
