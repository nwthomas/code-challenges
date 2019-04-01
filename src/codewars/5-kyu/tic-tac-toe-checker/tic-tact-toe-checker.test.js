const isSolved = require("./tic-tac-toe-checker");

describe("checks a Tic-Tac-Toe board for solutions", () => {
  it("checks for winning X and O solutions (1 and 2)", () => {
    const boardX = [[1, 0, 0], [0, 1, 2], [1, 2, 1]];
    const boardO = [[0, 2, 1], [1, 2, 0], [0, 2, 1]];
    expect(isSolved(boardX)).toBe(1);
    expect(isSolved(boardO)).toBe(2);
  });

  it("checks for an incomplete game", () => {
    const board = [[0, 0, 1], [1, 2, 0], [0, 2, 1]];
    expect(isSolved(board)).toBe(-1);
  });

  it("returns 0 if it's a cat's game where no one won", () => {
    const board = [[1, 2, 1], [1, 2, 1], [2, 1, 2]];
    expect(isSolved(board)).toBe(0);
  });
});
