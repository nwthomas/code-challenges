/*

Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

*/

class Node {
  constructor(value = null, left = null, right = null) {
    this._value = value;
    this._left = left;
    this._right = right;
  }
  getValue() {
    return this._value && this._value;
  }
  addValue(value, node = this) {
    if (typeof value !== "number" || node instanceof Node === false) {
      return false;
    }
    if (!this._value) {
      this._value = value;
      return true;
    }
    if (this.getValue() > value) {
      if (!this._left) {
        this._left = new Node(value);
        return true;
      } else {
        return this.addValue(value, this._left);
      }
    } else if (this.getValue() < value) {
      if (!this._right) {
        this._right = new Node(value);
        return true;
      } else {
        return this.addValue(value, this._right);
      }
    } else {
      return false;
    }
  }
}

function validateTree(headNode) {
  // finish
}

module.exports = { Node, validateTree };
