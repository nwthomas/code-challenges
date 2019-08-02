const meanderingArray = require("./meandering-array.js");

describe("Meandering Array code challenge", () => {
  describe("tests that an array of random numbers (including negative) returns in a biggest, smallest, second-biggest, second-smallest order", () => {
    it("should return a sorted array of numbers when a short array is passed as a parameter", () => {
      expect(meanderingArray([1, -3, 5, 2, 8, -9, -10])).toEqual([
        8,
        -10,
        5,
        -9,
        2,
        -3,
        1
      ]);
    });

    it("should return a sorted array of numbers when a long array is passed as a parameter", () => {
      expect(
        meanderingArray([
          1,
          2,
          3,
          4,
          5,
          6,
          7,
          8,
          9,
          -1,
          -2,
          -3,
          -4,
          -5,
          -6,
          -7,
          -8,
          -9
        ])
      ).toEqual([
        9,
        -9,
        8,
        -8,
        7,
        -7,
        6,
        -6,
        5,
        -5,
        4,
        -4,
        3,
        -3,
        2,
        -2,
        1,
        -1
      ]);
    });
  });
});
