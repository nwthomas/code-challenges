const copy = require("./deepCopyArray.js");

describe("copy()", () => {
  describe("should deep copy a simple array of data types", () => {
    it("tests that a deep copy of a simple array of integers has occurred", () => {
      const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9];
      expect(copy(arr)).toEqual(arr);
    });

    it("tests that a deep copy of simple array of strings has occurred", () => {
      const arr = ["1", "2", "3", "4", "5", "6", "7", "7", "8", "9"];
      expect(copy(arr)).toEqual(arr);
    });

    it("tests that a deep copy of a simple array of empty arrays has occured", () => {
      const arr = [[], [], [], []];
      expect(copy(arr)).toEqual(arr);
    });
  });

  describe("should deep copy a complex array with nested arrays", () => {
    it("tests that a deep copy of a complex, nested array has occured", () => {
      const arr = [1, 2, "dude", [5, 4, 8, [[[[[[[[[[[[[["End"]]]]]]]]]]]]]]]];
      expect(copy(arr)).toEqual(arr);
    });
  });
});
