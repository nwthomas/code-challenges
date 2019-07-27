const validParentheses = require("./valid-parentheses.js");

describe("Valid Parentheses CodeWars 8ky code challenge", () => {
  describe("tests that a string of parentheses passed as an argument is valid in a (()) pattern", () => {
    it("should take in a short string of valid parentheses and return a true boolean", () => {
      expect(validParentheses("(())")).toBeTruthy();
    });

    it("should take in a short string of invalid parentheses and return a false boolean", () => {
      expect(validParentheses("((())")).toBeFalsy();
    });

    it("should take in a long string of valid parentheses and return a true boolean", () => {
      expect(validParentheses("(((())))()((()()))")).toBeTruthy();
    });

    it("should take in a long string of invalid parentheses and return a false boolean", () => {
      expect(validParentheses("(((((()))))()((())()())))")).toBeFalsy();
    });
  });

  describe("tests that non-string and non-parentheses strings are handled correctly", () => {
    it("should take in a number as an argument and return a false boolean", () => {
      expect(validParentheses(8)).toBeFalsy();
    });

    it("should take in an object as an argument and return a false boolean", () => {
      expect(validParentheses({ test: "Test" })).toBeFalsy();
    });

    it("should take in an array as an argument and return a false boolean", () => {
      expect(validParentheses([1, 2, 3, 4, 5])).toBeFalsy();
    });

    it("should take in a boolean as an argument and return a false boolean", () => {
      expect(validParentheses(true)).toBeFalsy();
    });

    it("should take in NaN as an argument and return a false boolean", () => {
      expect(validParentheses(NaN)).toBeFalsy();
    });

    it("should take in undefined as an argument return a false boolean", () => {
      expect(validParentheses(undefined)).toBeFalsy();
    });

    it("should take in null as an argument and return a false boolean", () => {
      expect(validParentheses(null)).toBeFalsy();
    });

    it("should take in a string of non-parentheses characters and return a false boolean", () => {
      expect(validParentheses("This is a test.")).toBeFalsy();
    });
  });
});
