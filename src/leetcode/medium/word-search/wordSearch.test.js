const { wordSearch } = require("./wordSearch");

describe("wordSearch", () => {
    it("should return true if the word is found in the board", () => {
        const board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ];
        const word = "ABCCED";
        expect(wordSearch(board, word)).toBe(true);
    });

    it("should return true if the word is found in the board", () => {
        const board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ];
        const word = "SEE";
        expect(wordSearch(board, word)).toBe(true);
    });

    it("should return false if the word is not found in the board", () => {
        const board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"],
        ];
        const word = "ABCB";
        expect(wordSearch(board, word)).toBe(false);
    });
});
