/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.

For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.

Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

*/

const findNonDecreasingIntegers = array => {
  if (!array.length || typeof array !== "object") {
    return null;
  }
  let hasWrongValues = false;
  for (let i = 0; i < array.length; i++) {
    if (i && array[i] < array[i - 1]) {
      if (hasWrongValues) {
        return false;
      } else {
        hasWrongValues = true;
      }
    }
  }
  return true;
};

module.exports = findNonDecreasingIntegers;
