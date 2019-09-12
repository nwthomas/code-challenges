const copy = require("./deepCopy.js");

describe("copy()", () => {
  describe("should deep copy an object with simple key-value pairs", () => {
    it("tests if a deep copy of a simple object of number values has occured", () => {
      const obj = { 1: 1, 2: 2, 3: 3, 4: 4 };
      expect(copy(obj)).toEqual(obj);
    });

    it("tests if a deep copy of a simple object of string values has occured", () => {
      const obj = { "1": "1", "2": "2", "3": "3" };
      expect(copy(obj)).toEqual(obj);
    });
  });

  describe("should deep copy an object with nested objects inside of it", () => {
    it("tests if a deep copy of a complex, nested object has occured", () => {
      const obj = {
        1: 1,
        2: 2,
        3: { 4: 4, 5: { 6: 6, 7: { 8: { 9: { 10: 10 } } } } }
      };
      expect(copy(obj)).toEqual(obj);
    });
  });
});
