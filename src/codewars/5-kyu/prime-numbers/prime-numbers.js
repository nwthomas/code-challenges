/*

https://www.codewars.com/kata/52dd72494367608ac1000416

Preface
A prime number (or a prime) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

A more detailed description of prime numbers can be found at: http://en.wikipedia.org/wiki/Prime_number

The Problem
You will need to create logic for the following two functions: isPrime(number) and getPrimes(start, finish)

isPrime(number)
Should return boolean true if prime, otherwise false

getPrimes(start, finish)
Should return a unique, sorted array of all primes in the range [start, finish] (i.e. both numbers inclusive). Note that this range can go both ways - e.g. getPrimes(10, 1) should return all primes from 1 to 10 both inclusive.

Sample Input:
isPrime(number):
isPrime(0); // === false
isPrime(1); // === false
isPrime(2); // === true
isPrime(3); // === true
isPrime(4); // === false
isPrime(5); // === true

getPrimes(start, finish):
getPrimes(0, 0); // === []
getPrimes(0, 30); // === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
getPrimes(30, 0); // === [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

*/

function isPrime(number) {
  if (number <= 1) return false; // Returns false if number is less than or equal to 1
  for (let i = 2; i < number; i++) {
    if (number % i === 0) return false;
  }
  return true;
}

function getPrimes(start, finish) {
  const big = Math.max(start, finish);
  const small = Math.min(start, finish);
  let primes = [];
  for (let i = small; i <= big; i++) {
    const primeNum = isPrime(i);
    primeNum ? primes.push(i) : null;
  }
  return primes;
}

module.exports = { isPrime, getPrimes };
