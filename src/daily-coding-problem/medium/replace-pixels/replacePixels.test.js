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
    test("throws a new TypeError when the first argument is not an array", () => {
        const result = () => replacePixels("test", [1, 2], "G");
        expect(result).toThrow(
            TypeError("The 2D matrix must be an array with sub-arrays")
        );
    });

    test("throws a new TypeError when the first argument has no length", () => {
        const result = () => replacePixels([], [1, 2], "G");
        expect(result).toThrow(
            TypeError("The 2D matrix must be an array with sub-arrays")
        );
    });

    test("throws a new TypeError when the second argument is not an array", () => {
        const result = () =>
            replacePixels(
                [
                    [1, 2, 3],
                    [1, 2, 3]
                ],
                "test",
                "G"
            );
        expect(result).toThrow(
            TypeError("The point must be an array of two numbers")
        );
    });

    test("throws a new TypeError when the point does not contain numbers", () => {
        const result = () =>
            replacePixels(
                [
                    [1, 2],
                    [2, 1]
                ],
                [[], []],
                "G"
            );
        expect(result).toThrow(
            TypeError("The point must be an array of two numbers")
        );
    });

    test("throws a new TypeError when the point is an array longer than 2", () => {
        const result = () =>
            replacePixels(
                [
                    [1, 2],
                    [2, 1]
                ],
                [1, 2, 3, 4],
                "G"
            );
        expect(result).toThrow(
            TypeError("The point must exactly contain an X and Y axis")
        );
    });

    test("throws a new TypeError if the new color string is longer than 1", () => {
        const result = () =>
            replacePixels(
                [
                    [1, 2],
                    [2, 1]
                ],
                [1, 2],
                "test"
            );
        expect(result).toThrow(
            TypeError("The new color must be a string with one character")
        );
    });

    test("throws a new TypeError if the new color is not a string", () => {
        const result = () =>
            replacePixels(
                [
                    [1, 2],
                    [2, 1]
                ],
                [1, 0],
                {}
            );
        expect(result).toThrow(
            TypeError("The new color must be a string with one character")
        );
    });

    test("throws a new TypeError is the new color string is shorter than one character", () => {
        const result = () => replacePixels([1, 2], [2, 1], [0, 1], "");
        expect(result).toThrow(
            TypeError("The new color must be a string with one character")
        );
    });

    test("replaces a single pixel in an array", () => {
        const result = replacePixels(
            [
                ["G", "G", "R"],
                ["R", "Y", "G"],
                ["R", "G", "G"]
            ],
            [1, 1],
            "X"
        );
    });

    test("replaces a complex amount of pixels in an array", () => {
        const matrix = [
            ["G", "R", "R", "G", "R"],
            ["G", "R", "R", "G", "G"],
            ["R", "R", "G", "R", "G"],
            ["R", "G", "G", "G", "G"],
            ["R", "R", "R", "R", "R"]
        ];
        const changedMatrix = [
            ["G", "B", "B", "G", "R"],
            ["G", "B", "B", "G", "G"],
            ["B", "B", "G", "R", "G"],
            ["B", "G", "G", "G", "G"],
            ["B", "B", "B", "B", "B"]
        ];
        const result = replacePixels(matrix, [0, 1], "B");
        expect(result).toEqual(changedMatrix);
    });
});
