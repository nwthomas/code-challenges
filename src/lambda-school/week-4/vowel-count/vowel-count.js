/*

Write a function which counts the number of vowels in a given string. Return the count number.

Passing the string "Hello world!" as an argument to your vowelCount() function would result in the number 3 being returned.

For example:
console.log(vowelCount('-bcd-fgh-jklmn-pqrst-vwxyz')); // <--- 0
console.log(vowelCount('Hello world!')); // <--- 3
console.log(vowelCount('Pinto beans')); // <--- 4
console.log(vowelCount('The quick brown fox jumped over the lazy dog.')); // <--- 12
console.log(vowelCount('Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.')); // <--- 58
console.log(vowelCount('All I have ever wanted is to be an Uber driver!'

For the purposes of this exercise, we are not considering "y" as a vowel.

*/

function vowelCount(str) {
  let totalVowels = 0;
  let strArr = str.split("");
  let vowelsArr = "aeiouAEIOU".split("");
  for (let i = 0; i < strArr.length; i++) {
    for (let j = 0; j < vowelsArr.length; j++) {
      if (vowelsArr[j] === strArr[i]) {
        totalVowels += 1;
      }
    }
  }
  return totalVowels;
}

module.exports = vowelCount;
