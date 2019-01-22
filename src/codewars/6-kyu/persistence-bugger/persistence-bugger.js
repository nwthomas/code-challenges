/*

https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:
persistence(39) === 3 // because 3*9 = 27, 2*7 = 14, 1*4=4 and 4 only has one digit

persistence(999) === 4 // because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 - 12, and finally 1*2 = 2

persistence(4) === 0 // because 4 is already a one-digit number

*/

function persistence(num) {
  let nums = num.toString();
  let timesMultiplied = 0;
  while (nums.length > 1) {
    let total = parseInt(nums[0]);
    for (let i = 1; i < nums.length; i++) {
      total = total * parseInt(nums[i]);
    }
    timesMultiplied++;
    nums = total.toString();
  }
  return timesMultiplied;
}

module.exports = persistence;
