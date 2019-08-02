/*

Your photographer friend is wondering if you can help them decipher the white pixels on their latest photograph.  Write a function that takes in a matrix of 1s and 0s and returns the largest possible length of the side of a sub-square of 1s. The 1s represent white pixels, and the 0s represent black;

EXAMPLE:
const arr = [
  [1, 1, 1, 1, 0, 0], 
  [1, 1, 1, 1, 0, 0], 
  [1, 1, 1, 0, 0, 0], 
  [1, 0, 0, 1, 0, 0], 
  [1, 0, 0, 0, 1, 1]]; ---> Output of 3 from the 1s sub-matrix in the top-left part of the matrix.

*/

function largestMatrix(arr) {
  let squareLength = 0;
  const solutionArr = [[...Array(arr[0].length + 1)].map(x => 0), ...arr].map(
    (slot, index) => {
      return !index || index === arr.length + 2 ? slot : [0, ...slot];
    }
  );
  for (let i = 1; i < solutionArr.length; i++) {
    for (let j = 1; j < solutionArr[0].length; j++) {
      if (solutionArr[i][j]) {
        const spotTotal =
          Math.min(
            solutionArr[i][j - 1],
            solutionArr[i - 1][j],
            solutionArr[i - 1][j - 1]
          ) + 1;
        solutionArr[i][j] = spotTotal;
        if (spotTotal > squareLength) {
          squareLength = spotTotal;
        }
      }
    }
  }
  return squareLength;
}

module.exports = largestMatrix;
