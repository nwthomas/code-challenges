const duplicateCount = require("./counting-duplicates");

describe("duplicateCount()", () => {
  describe("tests how many times a string contains case-insensitive alphabetic and numeric chars", () => {
    it("should return 0 if no characters repeat more than once", () => {
      expect(duplicateCount("abcde")).toBe(0);
    });

    it("should return 2 if 2 duplicates are contained in the string", () => {
      expect(duplicateCount("a6Abhe6")).toBe(2);
    });

    it("should return the amount of duplicates despite each of those duplicates being present more than 2 times", () => {
      expect(duplicateCount("Indivisibilities")).toBe(2);
    });

    it("should return 1 when all spaces are passed into it", () => {
      expect(duplicateCount("          ")).toBe(1);
    });

    it("should be able to handle all upper case and all lower case", () => {
      expect(duplicateCount("DUDE")).toBe(1);
      expect(duplicateCount("dude")).toBe(1);
    });
  });
});
