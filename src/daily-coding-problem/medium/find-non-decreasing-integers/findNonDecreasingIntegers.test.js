const findNonDecreasingIntegers = require("./findNonDecreasingIntegers.js");

describe("findNonDecreasingIntegers", () => {
  describe("returns true", () => {
    test("should return true if an ordered array except for one integer is passed in", () => {
      const array = [1, 2, 3, 4, 5, 3, 7, 8];
      const result = findNonDecreasingIntegers(array);
      expect(result).toBeTruthy();
    });

    test("should return true for a long, ordered array with only one integer out of place", () => {
      const array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 2, 14, 15, 16];
      const result = findNonDecreasingIntegers(array);
      expect(result).toBeTruthy();
    });
  });

  describe("returns false", () => {
    test("should return false if an unordered array is passed in", () => {
      const array = [1, 2, 5, 7, 3, 9, 5, 10];
      const result = findNonDecreasingIntegers(array);
      expect(result).toBeFalsy();
    });

    test("should return false for a long, highly unordered array of integers", () => {
      const array = [1, 6, 9, 2, 7, 4, 345, 123, 789, 123, 456, 12, 1, 90];
      const result = findNonDecreasingIntegers(array);
      expect(result).toBeFalsy();
    });
  });

  describe("returns null", () => {
    test("should return null if a string is passed in", () => {
      const result = findNonDecreasingIntegers("test");
      expect(result).toBeNull();
    });

    test("should return null if an object is passed in", () => {
      const result = findNonDecreasingIntegers({});
      expect(result).toBeNull();
    });

    test("should return null if an integer is passed in", () => {
      const result = findNonDecreasingIntegers(1234);
      expect(result).toBeNull();
    });

    test("should return null if an empty array is passed in", () => {
      const result = findNonDecreasingIntegers([]);
      expect(result).toBeNull();
    });

    test("should return null if NaN is passed in", () => {
      const result = findNonDecreasingIntegers(NaN);
      expect(result).toBeNull();
    });
  });
});
