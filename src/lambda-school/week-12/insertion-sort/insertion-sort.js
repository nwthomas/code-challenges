/*

Insertion sort is a basic sorting algorithm.

Insertion sort iterates over an array, growing a sorted array behind the current location.

It takes each element from the input and finds the spot, up to the current point, where that element belongs.

It does this until it gets to the end of the array.

https://en.wikipedia.org/wiki/Insertion_sort

For example:
console.log(insertionSort([12, 44, 10, 2, 35, 1098, 356 ])); // <--- [2, 44, 10, 35, 356, 12, 1098]

*/

function insertionSort(array) {
  const elements = [...array];
  for (let i = 1; i < elements.length; i++) {
    for (let j = i; j > 0; j--) {
      if (elements[j] < elements[j - 1]) {
        [elements[j - 1], elements[j]] = [elements[j], elements[j - 1]];
      }
    }
  }
  return elements;
}

module.exports = insertionSort;
