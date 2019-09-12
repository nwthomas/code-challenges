/*

Give an object with a variable amount of keys and values (of any sort of data), write a custom copy function capable of deep-copying an object.

*/

function copy(oldObj) {
  const final = {};
  function helper(obj) {
    for (let key in obj) {
      if (typeof obj[key] === "object") {
        final[key] = copy(obj[key]);
      } else {
        final[key] = obj[key];
      }
    }
  }
  helper(oldObj);
  return final;
}

module.exports = copy;
