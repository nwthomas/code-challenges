const getRandomNumber = require("./randomNumberExceptList.js");

describe("randomNumberExceptList", () => {
  describe("getRandomNumber()", () => {
    test("returns null if the type of the first argument is not a number", () => {
      const result = getRandomNumber("test", [1, 2, 3, 4]);
      expect(result).toBeNull();
    });

    test("returns null if the first argument is less-than-or-equal-to 0", () => {
      const result = getRandomNumber(-1, [1, 2, 3, 4]);
      expect(result).toBeNull();
    });

    test("returns null if the type of the second argument is not an object", () => {
      const result = getRandomNumber(10, { test: "test" });
      expect(result).toBeNull();
    });

    test("returns a random number lesser than the number passed in and also not in the list", () => {
      const result = getRandomNumber(3, [0, 3]);
      expect(result).toBeOneOf([1, 2]);
    });
  });
});
