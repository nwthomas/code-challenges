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
  getAllTreeValues(node = this) {
    const values = [node.getValue()];
    if (node._left) {
      values.unshift(...this.getAllTreeValues(node._left));
    }
    if (node._right) {
      values.push(...this.getAllTreeValues(node._right));
    }
    return values;
  }
  addValue(value, node = this) {
    if (typeof value === "undefined" || node instanceof Node === false) {
      return null;
    }
    if (!node._value) {
      node._value = value;
      return true;
    }
    if (node.getValue() === value) {
      return true;
    } else if (node.getValue() > value) {
      if (node._left) {
        return node.addValue(value, node._left);
      } else {
        node._left = new Node(value);
        return true;
      }
    } else if (node.getValue() < value) {
      if (node._right) {
        return node.addValue(value, node._right);
      } else {
        node._right = new Node(value);
        return true;
      }
    } else {
      return false;
    }
  }
  validateTree(node = this) {
    if (node instanceof Node === false) {
      return null;
    }
    if (node._right && node._right.getValue() < node.getValue()) {
      return false;
    }
    if (node._left && node._left.getValue() > node.getValue()) {
      return false;
    }
    if (!node._left && !node._right) {
      return true;
    }
    if (node._right && node._right.getValue() > node.getValue()) {
      return this.validateTree(node._right);
    }
    if (node._left && node._left.getValue() < node.getValue()) {
      return this.validateTree(node._left);
    }
  }
}

module.exports = Node;
