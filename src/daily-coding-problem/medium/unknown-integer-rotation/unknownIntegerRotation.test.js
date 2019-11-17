const findRotatedNum = require("./unknownIntegerRotation.js");

describe("findRotatedNum()", () => {
  describe("should return null if the arguments are bad or the number can't be found", () => {
    it("tests that null is returned when the wrong argument is passed as first argument", () => {
      const result = findRotatedNum({ dude: "dude" }, 5);
      expect(result).toBe(null);
    });

    it("tests that null is returned when the wrong argument is passed as second argument", () => {
      const result = findRotatedNum([3, 6, 8, 9], "test");
      expect(result).toBe(null);
    });

    it("tests that null is returned when the number can't be found", () => {
      const result = findRotatedNum([4, 5, 6, 7, 8, 1, 2, 3], 10);
      expect(result).toBe(null);
    });
  });

  describe("should return the number from the list in less than linear time", () => {
    it("tests that the number is returned effectively", () => {
      const result = findRotatedNum([34, 56, 100, 1, 4, 6, 7, 9], 4);
      expect(result).toBe(4);
    });
  });
});
