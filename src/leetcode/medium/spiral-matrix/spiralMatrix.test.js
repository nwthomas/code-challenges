const { spiralOrder } = require("./spiralMatrix");

describe("spiralOrder", () => {
    it("returns the correct spiral order for a list with one array of one integer", () => {
        const result = spiralOrder([[0]]);
        expect(result).toEqual([0]);
    });

    it("returns the correct spiral order for a 2D matrix", () => {
        const result = spiralOrder([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]);
        expect(result).toEqual([1, 2, 3, 6, 9, 8, 7, 4, 5]);
    });
});
