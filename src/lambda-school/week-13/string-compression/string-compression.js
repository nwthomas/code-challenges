/*

Good morning! Implement a method to perform basic string compression using the counts of repeated characters.

For example, the string  'aabcccccaaa' would become a2b1c5a3.

If the "compressed" string would not become smaller than the original string, then your method should return the original string.

You can assume the string has only uppercase and lowercase letters (a - z).

*/

function stringCompression(str) {
  let compressed = [];
  let number = [];
  str.split("").forEach(char => {
    char === compressed[compressed.length - 1]
      ? number[number.length - 1]++
      : compressed.push(char) && number.push(1);
  });
  const finished = compressed
    .map((char, index) => char + number[index])
    .join("");
  return finished.length >= str.length ? str : finished;
}

module.exports = stringCompression;
