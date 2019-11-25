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

/**
 * 1. Check first array item top-down and left-right
 * 2. If the word is found, return true
 * 3. If not, move to the right and check again
 * 4. Should accomodate handling word length longer than array length
 */

function findWordInMatrix(arr, word) {
  // Checks the x axis of the 2D array for the word
  for (let i = 0; i < arr[0].length; i++) {
    let arrString = "";
    for (let j = 0; j < arr.length; j++) {
      arrString += arr[j][i];
    }
    const isWordMatched = arrString.toLowerCase().match(word.toLowerCase());
    if (isWordMatched) {
      return true;
    }
  }
  // Checks the x axis of the 2D array for the word
  for (let i = 0; i < arr.length; i++) {
    const arrString = arr[i].join("");
    const matched = arrString.toLowerCase().match(word.toLowerCase());
    if (matched && matched[0]) {
      return true;
    }
  }
  // Defaults to returning false if the word is not found
  return false;
}

module.exports = findWordInMatrix;
