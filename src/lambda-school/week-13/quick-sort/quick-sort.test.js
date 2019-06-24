const quickSort = require("./quick-sort");

describe("quickSort()", () => {
  describe("tests that arrays are sorted correctly using the quicksort algorithm", () => {
    it("should sort a number array using quicksort and return the sorted array", () => {
      expect(quickSort([10, 5, 2, 3, 6, 11, 1, 7, 1])).toEqual([
        1,
        1,
        2,
        3,
        5,
        6,
        7,
        10,
        11
      ]);
    });

    it("should account for lots of duplicate numbers and accurately return the sorted array", () => {
      expect(quickSort([9, 5, 5, 5, 5, 5, 1])).toEqual([1, 5, 5, 5, 5, 5, 9]);
    });

    it("should return the same array when an array with only one number is passed as an argument", () => {
      expect(quickSort([4])).toEqual([4]);
    });

    it("should return an empty array when an empty array is passed into it as an argument", () => {
      expect(quickSort([])).toEqual([]);
    });
  });
});
