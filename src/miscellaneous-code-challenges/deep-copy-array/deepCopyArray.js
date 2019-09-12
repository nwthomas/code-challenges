/*

Give an array with a variable amount of indexes and nested arrays inside it (of any sort of data), write a custom copy function capable of deep-copying an array.

*/

function copy(arr) {
  const final = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].length && typeof arr[i] === "object") {
      final[i] = copy(arr[i]);
    } else {
      final[i] = arr[i];
    }
  }
  return final;
}

module.exports = copy;
