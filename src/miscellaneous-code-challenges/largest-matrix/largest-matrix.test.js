const largestMatrix = require("./largest-matrix.js");

describe("Largest Matrix code challenge", () => {
  describe("tests that the length of the square of a sub-matrix is returned when a matrix of 1s and 0s is passed as an argument", () => {
    it("should return 3 when a matrix of 1s and 0s is passed as an argument", () => {
      expect(
        largestMatrix([
          [1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 0, 0],
          [1, 1, 1, 0, 0, 0],
          [1, 0, 0, 1, 0, 0],
          [1, 0, 0, 0, 1, 1]
        ])
      ).toBe(3);
    });

    it("should return 1 when a small matrix of 1s and 0x is passed as an argument", () => {
      expect(largestMatrix([[1, 0, 1], [0, 1, 1], [0, 0, 0]]));
    });

    it("should return 4 when a large matrix of 1s and 0s is passed as an argument", () => {
      expect(
        largestMatrix([
          [1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 0, 0],
          [1, 1, 1, 1, 0, 0],
          [1, 0, 0, 0, 1, 1]
        ])
      );
    });
  });
});
