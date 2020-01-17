/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a sorted list of integers, square the elements and give the output in sorted order.

For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].
*/

function squareAndSort(intArray) {
  if (!Array.isArray(intArray)) {
    throw new TypeError("The function argument must be an array of integers.");
  }
  if (!intArray.length) {
    return intArray;
  }
  const _squared = intArray.map(int => int * int);
  const _sorted = mergeSort(_squared);
  return _sorted;
}

function mergeSort(intArray) {
  if (!Array.isArray(intArray)) {
    throw new TypeError("The function argument must be an array of integers.");
  }
  if (intArray.length <= 1) {
    return intArray;
  }
  const _pivotIndex = Math.floor(Math.random() * intArray.length);
  const left = intArray.slice(0, _pivotIndex);
  const right = intArray.slice(_pivotIndex, intArray.length);
  return merge(mergeSort(left), mergeSort(right));
}

function merge(arr1, arr2) {
  if (!Array.isArray(arr1) || !Array.isArray(arr2)) {
    throw new TypeError("You must provide two arrays as arguments.");
  }
  const _final = [],
    _arr1 = [...arr1],
    _arr2 = [...arr2];
  while (_arr1.length || _arr2.length) {
    if (!_arr1.length) {
      _final.push(_arr2.shift());
    } else if (!_arr2.length) {
      _final.push(_arr1.shift());
    } else if (_arr2[0] <= _arr1[0]) {
      _final.push(_arr2.shift());
    } else if (_arr1[0] <= _arr2[0]) {
      _final.push(_arr1.shift());
    }
  }
  return _final;
}

module.exports = { squareAndSort, mergeSort, merge };
