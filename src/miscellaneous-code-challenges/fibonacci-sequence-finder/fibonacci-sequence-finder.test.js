const sumFibonacci = require("./fibonacci-sequence-finder");

describe("fibonacci()", () => {
  describe("should return the sum of all fibs", () => {
    it("tests if the correct sum has been returned for adding all fibs up to input number", () => {
      const result = sumFibonacci(20);
      expect(result).toBe(17710);
    });
  });

  describe("should handle non-integer arguments without breaking", () => {
    it("tests if null is returned when the argument is a non-integer", () => {
      const result = sumFibonacci("string");
      expect(result).toBe(null);
    });
  });

  describe("should return the correct fibonacci for an argument of less than 4", () => {
    it("tests if 0 is returned if the argument is 0", () => {
      const result = sumFibonacci(0);
      expect(result).toBe(0);
    });

    it("tests if 1 is returned if the argument is 1", () => {
      const result = sumFibonacci(1);
      expect(result).toBe(1);
    });

    it("tests if 2 is returned if the argument is 2", () => {
      const result = sumFibonacci(2);
      expect(result).toBe(2);
    });

    it("tests if 4 is returned if the argument is 3", () => {
      const result = sumFibonacci(3);
      expect(result).toBe(4);
    });
  });
});
