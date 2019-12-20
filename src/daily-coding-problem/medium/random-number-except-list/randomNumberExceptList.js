/*

Good morning! Here's your coding interview problem for today.

This question was asked by Google.

Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

*/

function getRandomNumber(n, l) {
  if (typeof n !== "number" || n <= 0 || typeof l !== "object" || !l.length) {
    return null;
  }
  const possibleNumbers = [];
  for (let i = 0; i <= n - 1; i++) {
    if (l.indexOf(i) === -1) {
      possibleNumbers.push(i);
    }
  }
  const guessedIndex = Math.floor(Math.random() * possibleNumbers.length);
  return possibleNumbers[guessedIndex];
}

module.exports = getRandomNumber;
