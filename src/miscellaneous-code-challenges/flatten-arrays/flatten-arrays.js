/*

FLATTEN ARRAYS

Write a function that takes in an array that may contain multiple other deeply nested arrays and flattens them out to the same level.

Example:
let uglyArray = [[3, [1, [8]], 9], 4]; // Should be [3, 1, 8, 9, 4]

*/

function flattenArrays(items) {
  const flattened = [];
  items.forEach(item => {
    if (Array.isArray(item)) {
      flattened.push(...flattenArrays(item));
    } else {
      flattened.push(item);
    }
  });
  return flattened;
}

module.exports = flattenArrays;
