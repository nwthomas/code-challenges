/*

Good morning! Write a function that accepts a tree data structure and a value to search for. Search for the value using a breadth-first search algorithm.

You can read about it here: https://en.wikipedia.org/wiki/Breadth-first_search

For example:
const tree = {
  x: { y: { z: { a: 2 } } },
  y: { z: { a: 2 } },
  z: { a: 2 },
  a: 2
};

breadthFirstSearch(tree, 2); will return true before it recursively searches the nested objects. Note that "recursively searching" does not mean that your algorithm requires a recursive function call.

While the strategy for your algorithm is to search by breadth first, you will want your algorithm capable of deeply searching nested objects.

For example:
let deep = {
  1: 2,
  3: {4: 'a', 'b': 'c'},
  5: {6: {7: 8}},
  9: {10: {11: {12: {13: {14: {15: 16}}}}}}
};

breadthFirstSearch(deep, 16); will return true.
breadthFirstSearch(deep, 'c'); will return true.

*/

function breadthFirstSearch(obj, searchTerm) {
  let queue = [],
    key;
  for (key in obj) queue.push(obj[key]);
  while (queue.length > 0) {
    let value = queue.shift();
    if (value === searchTerm) return true;
    if (typeof value === "object") {
      let nestedKey;
      for (nestedKey in value) queue.push(value[nestedKey]);
    }
  }
  return false;
}

module.exports = breadthFirstSearch;
