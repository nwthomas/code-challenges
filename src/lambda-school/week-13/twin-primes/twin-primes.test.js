const isTwinPrime = require("./twin-primes");

test("takes in a number and checks if it and the integers two numbers lesser and greater to it are primes", () => {
  expect(isTwinPrime(11)).toBe(true);
  expect(isTwinPrime(13)).toBe(true);
  expect(isTwinPrime(2)).toBe(false);
  expect(isTwinPrime(100)).toBe(false);
  expect(isTwinPrime(18709873)).toBe(false);
  expect(isTwinPrime(0)).toBe(false);
  expect(isTwinPrime(31)).toBe(true);
});
