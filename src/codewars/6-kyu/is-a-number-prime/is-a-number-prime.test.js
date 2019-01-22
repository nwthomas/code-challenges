const isPrime = require("./is-a-number-prime");

test("Takes in an integer and returns true/false depending on if it's prime or not", () => {
  expect(isPrime(5)).toBe(true);
  expect(isPrime(10)).toBe(false);
  expect(isPrime(530)).toBe(false);
  expect(isPrime(13)).toBe(true);
});
