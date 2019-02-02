/*

Good morning! Given a positive (or 0) number, return a string of 1's and 0's representing it's binary value:

toBinaryString(6) should return "110" (no leading 0).

Use of the native method number.toString(2);  is disallowed.

Count from 0 to 31 in binary with one hand: https://youtu.be/Bke95oWWZII

Remainder division with the modulo operator %

*/

function toBinaryString(number) {
  if (number === 0) return 0;
  let finalArray = [];
  for (; number; number >>= 1) {
    finalArray.unshift(number & 1);
  }
  return parseInt(finalArray.join(""));
}

module.exports = toBinaryString;
