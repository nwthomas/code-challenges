/*

Implement the quick sort sorting algorithm. Assume the input is an array of integers.

https://en.wikipedia.org/wiki/Quicksort

https://www.khanacademy.org/computing/computer-science/algorithms#quick-sort 

*/

function quickSort(array) {
  if (array.length <= 1) {
    return array; // Exit case
  } else {
    let pivot = [array[0]]; // Recursive case

    // Sub-array of all the elements less than the pivot
    const less = array.filter(num => num < pivot);

    // Takes into account possibility of duplicate number values
    const equal = array.filter(num => num === pivot[0]);

    // Sub-array of all the elements great than the pivot
    const greater = array.filter(num => num > pivot);
    return quickSort(less)
      .concat(equal)
      .concat(quickSort(greater));
  }
}

module.exports = quickSort;
