/*

Please write a function that will take in an array of random integers (including neagtive ones) and return an array with the biggest number first, smallest number second, second-biggest number third, second-smallest number fourth, etc.

EXAMPLES:
meanderingArray([3, 7, -2, 3, -8, 9]) // Should return [9, -8, 7, -2, 3, 3]
meanderingArray([4, -2, -3, 3]) // Should return [4, -3, 3, -2]

*/

function meanderingArray(unsorted) {
  const sorted = quickSort(unsorted);
  const finished = [];
  while (sorted.length) {
    const most = sorted.shift();
    let least;
    finished.push(most);
    if (sorted.length) {
      least = sorted.pop();
      finished.push(least);
    }
  }
  return finished;
}

function quickSort(data) {
  if (data.length <= 1) {
    return data;
  } else {
    const pivot = data[0];
    const lesser = data.filter(num => num < pivot);
    const equal = data.filter(num => num === pivot);
    const greater = data.filter(num => num > pivot);
    return quickSort(greater).concat(equal.concat(quickSort(lesser)));
  }
}

module.exports = meanderingArray;
