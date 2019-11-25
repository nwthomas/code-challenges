const findWordInMatrix = require("./wordMatrix.js");

describe("findWordInMatrix()", () => {
  const arr1 = [
    ["F", "A", "C", "I"],
    ["O", "B", "Q", "P"],
    ["A", "N", "O", "B"],
    ["M", "A", "S", "S"]
  ];

  const arr2 = [
    ["D", "F", "E", "R", "W", "V"],
    ["E", "R", "Q", "L", "K", "G"],
    ["N", "A", "T", "H", "A", "N"],
    ["N", "P", "I", "P", "O", "T"],
    ["C", "P", "B", "N", "F", "A"],
    ["N", "E", "A", "T", "E", "N"]
  ];

  describe("short 2D array", () => {
    it("should find words in a short 2D", () => {
      expect(findWordInMatrix(arr1, "FACI")).toBeTruthy();
      expect(findWordInMatrix(arr1, "FOAM")).toBeTruthy();
      expect(findWordInMatrix(arr1, "DUDE")).toBeFalsy();
    });
  });

  describe("long 2D array with multiple words", () => {
    it("should find multiple words in the same 2D array successfully", () => {
      expect(findWordInMatrix(arr2, "NEATEN")).toBeTruthy();
      expect(findWordInMatrix(arr2, "NATHAN")).toBeTruthy();
      expect(findWordInMatrix(arr2, "TESTS")).toBeFalsy();
    });
  });
});
