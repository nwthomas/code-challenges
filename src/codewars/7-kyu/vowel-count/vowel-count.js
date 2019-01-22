/*

https://www.codewars.com/kata/54ff3102c1bad923760001f3

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

The input string will only consist of lower case letters and/or spaces.

*/

function getCount(str) {
  let vowelsCount = 0;
  let vowels = ["a", "e", "i", "o", "u"];
  str.split("").forEach(letter => {
    vowels.forEach(vowel => {
      if (letter === vowel) vowelsCount++;
    });
  });
  return vowelsCount;
}

module.exports = getCount;
