/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.
*/

function Node(value = null, right = null, left = null) {
  /**
   * Creates a new instance of the Node class
   *
   * @param {any} value The value to be assigned to the current Node instance. It defaults to null.
   *
   * @param {Node} right The right value in the Binary Search Tree from the current Node, which is
   * equal-to-or-greater-than the current Node's value. It defaults to null.
   *
   * @param {Node} left The left value in the Binary Search Tree from the current Node, which is
   * lesser-than the current Node's value. It defaults to null.
   */

  this.value = value;
  this.left = left;
  this.right = right;
}

Node.prototype.addValue = function addValue(value = null, currentNode = this) {
  /**
   * Adds a value to the current Node if none exists or sorts through the Binary Search Tree
   * until the appropriate placement is found
   *
   * @param {any} value The value to be added to the Binary Search Tree. It defaults to null.
   *
   * @param {Node} currentNode While this parameter exists, it's advisable that you do not pass in a
   * Node as an argument. This is a parameter specifically included to call the method recursively
   * on itself. It defaults to the current node as referenced by the this keyword.
   */

  if (!currentNode.value) {
    currentNode.value = value;
  } else {
    if (value >= currentNode.value) {
      currentNode.right
        ? currentNode.addValue(value, currentNode.right)
        : (currentNode.right = new Node(value));
    }
    if (value < currentNode.value) {
      currentNode.left
        ? currentNode.addValue(value, currentNode.left)
        : (currentNode.left = new Node(value));
    }
  }
};

Node.prototype.verifyTreesAreSame = function verifyTreesAreSame(
  newTree = null,
  currentTree = this
) {
  /**
   * Checks if this tree and another one are the same structure
   *
   * @param {Node} newTree Takes in a Binary Search Tree to be verified against the head node of
   * the Binary Search Tree the method is being called against
   *
   * @param {Node} currentTree While this parameter exists, it's advisable that you do not pass
   * in a Node as an argument. This is a parameter specifically included to call the method
   * recursively on itself. It defaults to the current node as referenced by the this keyword.
   *
   * @returns {boolean} Returns true if the trees are the same or false otherwise
   */
  if (
    currentTree.value !== newTree.value ||
    newTree instanceof Node === false
  ) {
    return false;
  }
  if (
    !currentTree.left &&
    !currentTree.right &&
    !newTree.left &&
    !newTree.right
  ) {
    if (newTree.value === currentTree.value) {
      return true;
    }
  } else {
    let left, right;
    if (currentTree.left) {
      if (newTree.left) {
        left = currentTree.verifyTreesAreSame(newTree.left, currentTree.left);
      } else {
        left = false;
      }
    }
    if (currentTree.right) {
      if (newTree.right) {
        right = currentTree.verifyTreesAreSame(
          newTree.right,
          currentTree.right
        );
      } else {
        right = false;
      }
    }
    if ((left !== false && right !== false && left) || right) {
      return true;
    } else {
      return false;
    }
  }
};

module.exports = Node;
