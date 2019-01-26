const isPrime = require("./get-prime-numbers");

test("Takes in a number and returns a string stating whether or not it's a prime", () => {
  expect(isPrime(27)).toBe("27 is not a prime number.");
  expect(isPrime(11)).toBe("11 is a prime number.");
  expect(isPrime(67)).toBe("67 is a prime number.");
  expect(isPrime(-5)).toBe("Please enter a number greater than 0.");
});
