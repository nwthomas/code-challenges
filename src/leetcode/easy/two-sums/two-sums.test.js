const twoSum = require("./two-sums.js");

describe("Two Sums LeetCode code challenge", () => {
  describe("tests that an inputted array contains two numbers that add up to the target and returns their indices", () => {
    it("should take in a short array and return the indices of the numbers that add up to the target", () => {
      expect(twoSum([1, 5, 7, 3, 5], 8)).toEqual([0, 2]);
    });

    it("should take in a long array and return the indices of the numbers that add up to the target", () => {
      expect(
        twoSum([7, 4, 23, 6, 12, 3, 1, 1, 2, 8, 4, 234, 9, 2], 238)
      ).toEqual([1, 11]);
    });
  });
});
