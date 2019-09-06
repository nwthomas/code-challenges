const findMissingLetter = require("./find-the-missing-letter.js");

describe("findMissingLetter()", () => {
  describe("should return the missing lowercase letter in a short letter array sequence", () => {
    it("tests that a missing letter of Q is returned when it's missing in an array sequence", () => {
      expect(findMissingLetter(["m", "n", "o", "p", "r"])).toBe("q");
    });

    it("tests that a missing letter of c is returned when it's missing in an array sequence", () => {
      expect(findMissingLetter(["b", "d"])).toBe("c");
    });
  });

  describe("should return the missing uppercase letter in a short letter array sequence", () => {
    it("tests that a missing letter of D is returned when it's missing in an array sequence", () => {
      expect(findMissingLetter(["A", "B", "C", "E"])).toBe("D");
    });

    it("tests that a missing letter of X is returned when it's missing in an array sequence", () => {
      expect(findMissingLetter(["W", "Y", "Z"])).toBe("X");
    });
  });

  describe("should return the missing letter in a long letter array sequence", () => {
    it("tests that a missing letter of n is returned in a completed array of the alphabet", () => {
      const arr = "abcdefghijklmopqrstuvwxyz".split("");
      expect(findMissingLetter(arr)).toBe("n");
    });
  });
});
