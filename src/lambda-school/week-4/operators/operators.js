/*

Good morning! Implement four functions called multiply, divide, modulo, and negCheck. The first three functions should multiply, divide, or return the remainder of two arguments after invoking negCheck upon the two numbers.

Now for the tricky part: you can only use + and - to implement these functions.
Do not use the JavaScript operators for multiply, divide and modulo: * / %

The negCheck function needs to indicate whether or not the resulting product, quotient and remainder would be positive or negative. Use a Boolean value to indicate this (you can use the not operator ! to toggle the Boolean value.) negCheck should return an array with that Boolean having converted num1 and num2 into positive integers.

Hint: divide should drop the remainder.
NOTE: the test suite will check to see if you are using the * / or % operators. This test will fail if you have commented out code within your functions.

For example:

console.log(negCheck(12, 34)); //   <--- [ false, 12, 34 ]
console.log(negCheck(-12, 34)); //  <--- [ true, 12, 34 ]
console.log(negCheck(12, -34)); //  <--- [ true, 12, 34 ]
console.log(negCheck(-12, -34)); // <--- [ false, 12, 34 ]
console.log(multiply(3, 4)); //     <--- 12
console.log(multiply(-3, 4)); //    <--- -12
console.log(multiply(3, -4)); //    <--- -12
console.log(multiply(-3, -4)); //   <--- 12
console.log(divide(10, 3)); //      <--- 3
console.log(divide(-10, 3)); //     <--- -3
console.log(divide(10, -3)); //     <--- -3
console.log(divide(-10, -3)); //    <--- 3
console.log(modulo(10, 3)); //      <--- 1
console.log(modulo(-10, 3)); //     <--- -1
console.log(modulo(10, -3)); //     <--- 1
console.log(modulo(-10, -3)); //    <--- -1

*/

function negCheck(num1, num2) {
  if ((num1 < 0 && num2 < 0) || (num1 > 1 && num2 > 0)) {
    return false;
  } else {
    return true;
  }
}

function multiply(x, y) {
  const arr = negCheck(x, y);
  let total = 0;
  for (let i = 0; i < Math.abs(y); i++) {
    total += Math.abs(x);
  }
  return arr ? (total ? -total : total) : total;
}

function divide(x, y) {
  const arr = negCheck(x, y);
  let dividend = Math.abs(x);
  let quotient = 0;
  while (dividend >= Math.abs(y)) {
    quotient++;
    dividend -= Math.abs(y);
  }
  return arr ? -quotient : quotient;
}

function modulo(x, y) {
  let dividend = Math.abs(x);
  while (dividend >= Math.abs(y)) {
    dividend -= Math.abs(y);
  }
  return dividend;
}

module.exports = {
  negCheck,
  multiply,
  divide,
  modulo
};
