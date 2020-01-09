/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
*/

class Node {
  constructor(value = null, left = null, right = null) {
    this._value = value;
    this._left = left;
    this._right = right;
  }

  getValue() {
    /**
     * Returns the value of the current Node
     */
    return this._value;
  }

  addValue(value = null, current = this) {
    /**
     * Adds a new value in a Node to Binary Search Tree using recursion
     */
    if (value === null || typeof value !== "number") {
      return false;
    }
    if (!this.getValue()) {
      this._value = value;
      return true;
    } else {
      if (value <= current.getValue()) {
        if (current._left) {
          return current.addValue(value, current._left);
        } else {
          current._left = new Node(value);
          return true;
        }
      } else if (value > current.getValue()) {
        if (current._right) {
          return current.addValue(value, current._right);
        } else {
          current._right = new Node(value);
          return true;
        }
      } else {
        return false;
      }
    }
  }

  getLeafPaths() {
    /**
     * Returns all possible valid leaf paths in the form of an array of arrays
     */
    const finished = [];

    function getPaths(currentNode, currentPath) {
      const newPath = [...currentPath];
      currentNode.getValue() !== null && newPath.push(currentNode.getValue());
      if (currentNode._left) {
        getPaths(currentNode._left, newPath);
      }
      if (currentNode._right) {
        getPaths(currentNode._right, newPath);
      }
      if (!currentNode._left && !currentNode._right && newPath.length) {
        finished.push(newPath);
      }
    }

    getPaths(this, []);

    return finished;
  }
}

module.exports = Node;
