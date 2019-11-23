/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

 and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

*/

function findWordInMatrix(arrayOfLetters, searchWord) {
  let found = false,
    word = "",
    x = 0,
    y = 0,
    letterIndex = 0;
  if (
    arrayOfLetters.length >= searchWord.length ||
    arrayOfLetters[0].length >= searchWord.length
  ) {
    return found;
  }
}

module.exports = findWordInMatrix;
