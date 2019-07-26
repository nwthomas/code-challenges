const { negCheck, multiply, divide, modulo } = require("./operators.js");

describe("Operators Lambda School code challenge", () => {
  describe("tests that the negCheck() function returns a boolean properly", () => {
    it("should return a false value if the numbers passed in as arguments are both positive", () => {
      expect(negCheck(10, 6518254)).toBeFalsy();
    });

    it("should return a false value if both the numbers passed in as arguments are negative", () => {
      expect(negCheck(-67458, -1)).toBeFalsy();
    });

    it("should return a true value if either one of the arguments are negative", () => {
      expect(negCheck(-5, 10)).toBeTruthy();
      expect(negCheck(567, -4)).toBeTruthy();
    });
  });

  describe("tests that the multiply() function returns the product without using the * operator", () => {
    it("should take in two positive numbers as arguments and return the product", () => {
      expect(multiply(10, 10)).toBe(100);
    });

    it("should take in a negative and a positive number as arguments and return the product", () => {
      expect(multiply(-4, 50)).toBe(-200);
    });

    it("should take in two negative numbers as arguments and return the product", () => {
      expect(multiply(-20, 100)).toBe(-2000);
    });
  });

  describe("tests that the divide() function returns the quotient without using the / operator", () => {
    it("should take in two positive numbers as arguments and return a positive quotient", () => {
      expect(divide(10, 2)).toBe(5);
    });

    it("should take in a negative and positive number as arguments and return a negative quotient", () => {
      expect(divide(-10, 2)).toBe(-5);
    });

    it("should take in two negative numbers as arguments and return a positive quotient", () => {
      expect(divide(-40, -20)).toBe(2);
    });
  });

  describe("tests that the modulo() function returns the remainder without using the / operator", () => {
    test("should take in two positive numbers and return a remainder", () => {
      expect(modulo(40, 7)).toBe(5);
    });

    test("should take in a negative and a positive number and return a remainder", () => {
      expect(modulo(-100, 11)).toBe(1);
    });

    test("should take in two negative numbers and return a remainder", () => {
      expect(modulo(-50, -6)).toBe(2);
    });
  });
});
