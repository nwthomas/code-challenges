const { CountSquares } = require("./countSquares");

describe("CountSquares", () => {
    it("should return the correct number of squares", () => {
        const count_squares = new CountSquares();
        count_squares.add([1, 1]);
        count_squares.add([1, 2]);
        count_squares.add([2, 1]);
        count_squares.add([2, 2]);
        count_squares.add([2, 2]);

        expect(count_squares.count([1, 1])).toBe(2);
        expect(count_squares.count([1, 2])).toBe(2);
        expect(count_squares.count([2, 1])).toBe(2);
        expect(count_squares.count([2, 2])).toBe(1);
    });
});
