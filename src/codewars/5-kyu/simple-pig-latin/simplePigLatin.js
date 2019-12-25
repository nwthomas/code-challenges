/*

https://www.codewars.com/kata/simple-pig-latin/javascript

Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.

Examples
pigIt('Pig latin is cool'); // igPay atinlay siay oolcay
pigIt('Hello world !');     // elloHay orldway !

*/

function pigIt(str) {
  if (typeof str !== "string") {
    return null;
  }
  const final = [];
  const strArr = str.split(" ");
  const punctuations = /[!@#$%^&*()_+-={}:";'<>?,.?~`]/i;
  strArr.forEach(word => {
    if (word.match(punctuations)) {
      final.push(word);
    } else {
      const temp = word.slice(1, word.length) + word[0] + "ay";
      final.push(temp);
    }
  });
  return final.join(" ");
}

module.exports = pigIt;
