const { readN, read7 } = require("./readSevenNTimes.js");

describe("readSevenNTimes", () => {
  describe("read7", () => {
    test("should return null when a non-string is passed as an argument", () => {
      const result = read7(1234);
      expect(result).toBeNull();
    });

    test("should return the first seven characters of a string passed in", () => {
      const result = read7("testing testing testing");
      expect(result).toBe("testing");
    });

    test("should handle strings less than 7 characters in length", () => {
      const result = read7("test");
      expect(result).toBe("test");
    });
  });

  describe("readN", () => {
    test("should return null when a non-string is passed as the file argument", () => {
      const result = readN(3, []);
      expect(result).toBeNull();
    });

    test("should return null when a non integer is passed as the number argument", () => {
      const result = readN("test", "test");
      expect(result).toBeNull();
    });

    test("should return null if n iterations is less than 0", () => {
      const result = readN(-10, "test");
      expect(result).toBeNull();
    });

    test("should return the first seven digits of a string in an array when the number of iterations is 1", () => {
      const result = readN(1, "testing testing testing");
      expect(result).toEqual(["testing"]);
    });

    test("should return an array of 7 characters when a long string is passed in", () => {
      const result = readN(
        5,
        "My name is Nathan Thomas and this is a test of my code."
      );
      expect(result).toEqual([
        "My name",
        " is Nat",
        "han Tho",
        "mas and",
        " this i"
      ]);
    });

    test("should handle a short string passed in with a large number of n iterations", () => {
      const result = readN(10, "test");
      expect(result).toEqual(["test", "", "", "", "", "", "", "", "", ""]);
    });
  });
});
