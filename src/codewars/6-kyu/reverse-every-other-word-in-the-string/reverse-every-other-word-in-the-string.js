/*

Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are apart of the word in this kata.

*/

function reverse(str){
  return str.trim().split(" ").map((word, index) => {
    if (index % 2) {
      return word.split("").reverse().join("");
    } else {
      return word;
    }
  }).join(" ");
}

module.exports = reverse;