const { setMatrixZeroes } = require("./setMatrixZeroes.js");

describe("setMatrixZeroes", () => {
    it("does not modify the original matrix if there are no zeroes", () => {
        const result = setMatrixZeroes([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]);
        expect(result).toEqual([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]);
    });

    it("modifies the original matrix if there are zeroes", () => {
        const result = setMatrixZeroes([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]);
        expect(result).toEqual([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]);
    });
});
