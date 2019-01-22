/*

Good morning! Write a function that takes in a string, reverses the 'casing' of that string, and returns the "reversed-casing" string.

const string = 'HELLO world!';
console.log(reverseCase(string)); // <--- hello WORLD!

*/

function reverseCase(str) {
  let caseSwitchedArr = [];
  for (i = 0; i < str.length; i++) {
    if (str[i] === str[i].toUpperCase()) {
      caseSwitchedArr.push(str[i].toLowerCase());
    } else if (str[i] === str[i].toLowerCase()) {
      caseSwitchedArr.push(str[i].toUpperCase());
    } else {
      alert("Something went wrong!");
    }
  }
  return caseSwitchedArr.join("");
}

module.exports = reverseCase;
