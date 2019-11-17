/*

FIBONACCI SEQUENCE FINDER

Write a function that returns the sum of the fibonacci numbers under-and-including a number input into the function as a parameter.

Example:
fibonacci(20); // Should return 17710
fibonacci(10); // Should return 143

*/

function sumFibonacci(n) {
  if (typeof n !== "number") return null;
  if (n <= 3) {
    if (n <= 0) return 0;
    if (n === 1) return 1;
    if (n === 2) return 2;
    if (n === 3) return 4;
  }
  let fibs = [1, 2];
  let total = 4;
  function findNextFib() {
    return fibs[1] + fibs[0];
  }
  for (let i = 4; i <= n; i++) {
    const newFib = findNextFib();
    fibs = [fibs[1], newFib];
    total += newFib;
  }
  return total;
}

module.exports = sumFibonacci;
