/*

Write a function, isPrime(), that takes in a number and returns a string saying whether or not the number is a prime.

If prime, it should return "{num} is a prime number."

If not prime, it should return "{num} is not a prime number."

If the number is less than 1, it should return "Please enter a number greater than 0."

*/

function isPrime(num) {
  let isPrime = "";
  if (num <= 0) return "Please enter a number greater than 0.";
  for (i = 2; i < num; i++) {
    if (num % i === 0) {
      isPrime = num + " is not a prime number.";
    }
  }
  return isPrime ? isPrime : `${num} is a prime number.`;
}

module.exports = isPrime;
