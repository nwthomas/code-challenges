const shortenUrl = require("./urlShortener.js");
const [shorten, restore] = shortenUrl(6);

describe("urlShortener()", () => {
  describe("should take in a string url and return a shortened one", () => {
    it("tests that a shortened url has been returned", () => {
      const originalUrl = "facebook.com/kljahsdklfjgajkshdgfkjas".split("/");
      const result = shorten(originalUrl[1]);
      expect(typeof result).toBe("string");
    });

    it("tests that the correct length of shortened Url is returned", () => {
      const originalUrl = "ajshgdfljahgskdjfhgasdf";
      const result = shorten(originalUrl);
      expect(result.length).toBe(6);
    });
  });

  describe("should handle wrong primitive types being passed in without breaking", () => {
    it("tests that a null value is returned when a non-number is passed into shortenUrl", () => {
      const result = shortenUrl("string");
      expect(result).toBe(null);
    });

    it("tests that a null value is returned when a non-string is passed into shorten", () => {
      const result1 = shorten(6);
      expect(result1).toBe(null);
      const result2 = shorten({});
      expect(result2).toBe(null);
    });

    it("tests that a null value is returned when a non-string is passed into restore", () => {
      const result = restore(162783);
      expect(result).toBe(null);
    });
  });

  describe("should return the correct old url when restore is called", () => {
    it("tests that the old url is returned correctly", () => {
      const original = "ajsghdflkhasdklfjhaslkdfjhasdf";
      const shortened = shorten(original);
      const result = restore(shortened);
      expect(result).toBe(original);
    });
  });
});
