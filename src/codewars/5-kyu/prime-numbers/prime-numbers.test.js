const { isPrime, getPrimes } = require("./prime-numbers");

test("checks if given number is prime", () => {
  expect(isPrime(0)).toBe(false);
  expect(isPrime(1)).toBe(false);
  expect(isPrime(2)).toBe(true);
  expect(isPrime(3)).toBe(true);
  expect(isPrime(4)).toBe(false);
  expect(isPrime(5)).toBe(true);
  expect(isPrime(6)).toBe(false);
  expect(isPrime(53)).toBe(true);
  expect(isPrime(893027189)).toBe(false);
});

test("takes in two numbers and finds all the prime numbers between them", () => {
  expect(getPrimes(0, 0).join()).toBe("");
  expect(getPrimes(0, 30).join()).toBe("2,3,5,7,11,13,17,19,23,29");
  expect(getPrimes(30, 0).join()).toBe("2,3,5,7,11,13,17,19,23,29");
});
