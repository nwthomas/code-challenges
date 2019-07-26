const chainedFunctions = require("./chained-functions.js");

describe("Chained Functions Lambda School code challenge", () => {
  describe("tests that an array of functions and a number are curried in and invoked", () => {
    it("should take in an array of functions and a number and return the total", () => {
      const one = x => {
        return x * 2;
      };
      const two = x => {
        return x * x;
      };
      expect(chainedFunctions([one, two])(3)).toBe(36);
    });

    it("should take in an array of functions and a string and return the concatenated string", () => {
      const one = x => {
        return "Hello " + x + ", ";
      };
      const two = x => {
        return x + "this is totally a test.";
      };
      expect(chainedFunctions([one, two])("Nathan")).toBe(
        "Hello Nathan, this is totally a test."
      );
    });

    it("should take in a very long array of functions and a number and return the total", () => {
      const one = x => x + 1;
      const two = x => x + 2;
      const three = x => x + 3;
      const four = x => x + 4;
      const five = x => x + 5;
      const arr = [one, two, three, four, five];
      expect(chainedFunctions(arr)(1)).toBe(16);
    });
  });
});
