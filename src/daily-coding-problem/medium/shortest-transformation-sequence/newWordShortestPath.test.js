const findShortestTransformationSequence = require("./newWordShortestPath.js");

describe("findShortestTransformationSequence()", () => {
    test("throws a new TypeError when the first argument is not a string", () => {
        const result = () =>
            findShortestTransformationSequence({}, "test", ["test"]);
        expect(result).toThrow(
            TypeError(
                "The first argument of findShortestTransformationSequence must be a string"
            )
        );
    });

    test("throws a new TypeError when the second argument is not a string", () => {
        const result = () =>
            findShortestTransformationSequence("test", {}, ["test"]);
        expect(result).toThrow(
            TypeError(
                "The second argument of findShortestTransformationSequence must be a string"
            )
        );
    });

    test("throws a new TypeError when the third argument is not an array", () => {
        const result = () =>
            findShortestTransformationSequence("test", "nate", {});
        expect(result).toThrow(
            TypeError(
                "The third argument of findShortestTransformationSequence must be an object"
            )
        );
    });

    test("returns null if the array of words is length 0", () => {
        const result = findShortestTransformationSequence("nate", "test", []);
        expect(result).toBeNull();
    });

    test("returns null if no path can be found in the word array", () => {
        const result = findShortestTransformationSequence("dog", "cat", [
            "nate",
            "test",
            "doggie"
        ]);
        expect(result).toBeNull();
    });

    test("returns the correct change path if one exists between start and ending words", () => {
        const result = findShortestTransformationSequence("dog", "cat", [
            "dot",
            "dat",
            "test",
            "testing"
        ]);
        expect(result).toEqual(["dog", "dot", "dat", "cat"]);
    });
});
