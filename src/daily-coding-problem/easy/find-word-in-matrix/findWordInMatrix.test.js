const { findWordInMatrix, isWordPresent } = require("./findWordInMatrix");

const mockMatrix = [
    ["F", "O", "M", "A", "L", "F"],
    ["O", "A", "O", "Z", "T", "A"],
    ["A", "R", "M", "T", "H", "Y"],
    ["M", "I", "Q", "E", "Y", "K"],
    ["W", "P", "F", "K", "S", "X"],
];

describe("find word in matrix", () => {
    describe("findWordInMatrix function", () => {
        test('finds the word "FOAM" in the y axis of the matrix', () => {
            const result = findWordInMatrix(mockMatrix, "FOAM");
            expect(result).toBe(true);
        });

        test('finds the word "ARM" in the x axis of the matrix', () => {
            const result = findWordInMatrix(mockMatrix, "ARM");
            expect(result).toBe(true);
        });

        test('does not find the word "JOY" in either of the axes of the matrix', () => {
            const result = findWordInMatrix(mockMatrix, "JOY");
            expect(result).toBe(false);
        });
    });
});
