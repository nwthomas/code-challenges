/*

Good morning! Write a function called reverseNumber that reverses a number.

Input Example: 
12345
555

Output Example:  
54321
555

*/

function reverseNumber(num) {
  let reversedNum = num
    .toString()
    .split("")
    .reverse()
    .join("");
  return parseInt(reversedNum);
}

module.exports = reverseNumber;
