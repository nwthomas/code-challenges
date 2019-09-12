/*

Give an array with a variable amount of indexes and nested arrays inside it (of any sort of data), write a custom copy function capable of deep-copying an array.

*/

function copy(oldArr) {
  const final = [];
  function helper(arr) {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].length && typeof arr[i] === "object") {
        final[i] = copy(arr[i]);
      } else {
        final[i] = arr[i];
      }
    }
  }
  helper(oldArr);
  return final;
}

module.exports = copy;
