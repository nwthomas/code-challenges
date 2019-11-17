const maxWords = require("./maximumPossibleWords.js");

describe("maxWords()", () => {
  describe("should handle the wrong arguments primitives being passed in", () => {
    it("tests that null is returned for non-string types", () => {
      const result = maxWords([], 100);
      expect(result).toBe(null);
    });

    it("tests that null is returned for non-integer types", () => {
      const result = maxWords("correct string", "wrong string");
      expect(result).toBe(null);
    });
  });

  describe("should return an empty array if the length for each small string is impossible to make", () => {
    it("tests if the desired length of each smaller maximum string is possible", () => {
      const result = maxWords(
        "maximum capabilities testing craziness absolutely",
        4
      );
      expect(result).toEqual([]);
    });
  });

  describe("should return an array with maximum length strings", () => {
    it("tests that a maximum array of sub-strings has been returned", () => {
      const result = maxWords("This is a test of the function", 8);
      expect(result).toEqual(["This is", "a test", "of the", "function"]);
    });

    it("tests that it will place maximum possible words in each string", () => {
      const result = maxWords("Test test test test test test test", 30);
      expect(result).toEqual(["Test test test test test test", "test"]);
    });
  });
});
