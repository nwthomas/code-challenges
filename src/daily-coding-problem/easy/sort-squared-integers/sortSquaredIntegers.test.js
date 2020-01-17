const { squareAndSort, mergeSort, merge } = require("./sortSquaredIntegers.js");

describe("sortSquaredIntegers", () => {
  describe("merge()", () => {
    test("merges two sorted arrays of integers together in order", () => {
      const arr1 = [1, 2, 4, 6, 7];
      const arr2 = [5, 7, 9, 10];
      const result = merge(arr1, arr2);
      expect(result).toEqual([1, 2, 4, 5, 6, 7, 7, 9, 10]);
    });

    test("throws a TypeError when the function is called with invalid types as arguments", () => {
      const result = () => merge("test1", "test2");
      expect(result).toThrow(
        new TypeError("You must provide two arrays as arguments.")
      );
    });
  });

  describe("mergeSort()", () => {
    test("sorts an unsorted array of integers using the merge sort algorithm", () => {
      const result = mergeSort([4, 8, 1, 4, 567, 123, 10, 9, 5, 3]);
      expect(result).toEqual([1, 3, 4, 4, 5, 8, 9, 10, 123, 567]);
    });

    test("returns an empty array when it is passed an empty array as an argument", () => {
      const result = mergeSort([]);
      expect(result).toEqual([]);
    });

    test("throws a TypeError when the function is called with invalid types as arguments", () => {
      const result = () => mergeSort("test");
      expect(result).toThrow(
        new TypeError("The function argument must be an array of integers.")
      );
    });
  });

  describe("squareAndSort()", () => {
    test("throws a TypeError when the function is called with a type other than array as argument", () => {
      const result = () => squareAndSort("test");
      expect(result).toThrow(
        new TypeError("The function argument must be an array of integers.")
      );
    });

    test("returns an empty array when it is passed an empty array as an argument", () => {
      const result = squareAndSort([]);
      expect(result).toEqual([]);
    });

    test("returns a squared and sorted array of integers", () => {
      const result = squareAndSort([4, 8, 1, 3, 0, 5, 8]);
      expect(result).toEqual([0, 1, 9, 16, 25, 64, 64]);
    });
  });
});
