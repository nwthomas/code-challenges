const sortArray = require("./sort-odd-and-even-numbers-in-different-order");

describe("sortArray()", () => {
  describe("tests that odd nums are sorted in ascending order and even nums in descending", () => {
    it("should return an empty array if one is passed to it as an argument", () => {
      expect(sortArray([])).toEqual([]);
    });

    it("should return the original array if passed an array with only one number value", () => {
      expect(sortArray([35])).toEqual([35]);
    });

    it("should sort an array of odd and even digits", () => {
      expect(sortArray([1, 80, 3, 4, 6, 17, 18, 8])).toEqual([
        1,
        80,
        3,
        18,
        8,
        17,
        6,
        4
      ]);
    });

    it("should sort another array of odd and even digits", () => {
      expect([5, 3, 2, 8, 1, 4]).toEqual([5, 3, 2, 8, 1, 4]);
    });
  });
});
