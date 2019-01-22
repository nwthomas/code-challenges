/*

Good morning! Complete the function so that it converts dash-delimited ("kebab" case) & underscore-delimited ("snake" case) words into "camel" casing. The first word within the output should be capitalized only if the original word was capitalized.

toCamelCase("the-stealth-warrior") // returns "theStealthWarrior"

toCamelCase("The_stealth_warrior") // returns "TheStealthWarrior"

*/

function toCamelCase(str) {
  let strArr = str.split("");
  for (i = 0; i < strArr.length; i++) {
    if (strArr[i] === "_" || strArr[i] === "-") {
      strArr[i] = " ";
    }
  }
  strArr = strArr.join("").split(" ");
  return strArr
    .map(function(word) {
      if (word === strArr[0]) return word;
      return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
    })
    .join("");
}

module.exports = toCamelCase;
