const insertionSort = require("./insertion-sort.js");

describe("insertionSort()", () => {
  describe("should sort a short array of integers successfully", () => {
    it("tests that a short array of integers is sorted successfully", () => {
      expect(insertionSort([3, 7, 12, 9])).toEqual([3, 7, 9, 12]);
    });
  });

  describe("should sort a long array of integers successfully", () => {
    it("tests that a long array of integers is sorted succesfully", () => {
      const arr = [6, 2, 9, 22, 65, 3987, 4, 6, 3, 110];
      expect(insertionSort(arr)).toEqual([2, 3, 4, 6, 6, 9, 22, 65, 110, 3987]);
    });
  });

  describe("should sort an array of floating point number successfully", () => {
    it("tests that an array of floating point numbers is sorted successfully", () => {
      const arr = [44.22222, 66.66666, 198.57182, 1826391.1];
      expect(insertionSort(arr)).toEqual([
        44.22222,
        66.66666,
        198.57182,
        1826391.1
      ]);
    });
  });
});
