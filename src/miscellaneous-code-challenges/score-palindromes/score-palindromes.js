/*

SCORE PALINDROMES

Write a function that takes in a string and returns a score of how many letters are the same when the string is reversed.

The palindrome does not need to be case sensitive (i.e. "t" versus "T").

https://en.wikipedia.org/wiki/Palindrome

*/

function scorePalindrome(word) {
  let score = 0;
  let normalWord = word.toLowerCase();
  let reverseWord = normalWord
    .split("")
    .reverse()
    .join("");
  for (i = 0; i < normalWord.length; i++) {
    if (normalWord[i] === reverseWord[i]) {
      score += 1;
    }
  }
  return score;
}

module.exports = scorePalindrome;
