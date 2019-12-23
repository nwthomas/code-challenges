/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a binary tree of integers, find the maximum path sum between two nodes. 

The path must go through at least one node, and does not need to go through the root.

*/

class Node {
  constructor(value = null, left = null, right = null) {
    this._value = value;
    this._left = left;
    this._right = right;
  }

  getValue() {
    return this._value;
  }

  addValue(value) {
    if (typeof value === "undefined") {
      return null;
    }
    if (!this.getValue()) {
      current._value = value;
    }
    let current = this;
    while (current) {
      if (value === current.getValue()) {
        return true;
      } else if (value > current.getValue()) {
        if (current._right) {
          current = current._right;
        } else {
          current._right = new Node(value);
          return true;
        }
      } else if (value < current.getValue()) {
        if (current._left) {
          current = current._left;
        } else {
          current._left = new Node(value);
          return true;
        }
      } else {
        return false;
      }
    }
  }

  getValuesBetweenNodes(searchValue, currentNode = this, values = []) {
    const valuesArray = values.concat(currentNode.getValue());
    if (typeof searchValue === "undefined") {
      return null;
    }
    if (searchValue === currentNode.getValue()) {
      return valuesArray;
    } else if (searchValue > currentNode.getValue()) {
      if (currentNode._right) {
        return currentNode._right.getValuesBetweenNodes(
          searchValue,
          currentNode._right,
          valuesArray
        );
      } else {
        return [];
      }
    } else if (searchValue < currentNode.getValue()) {
      if (currentNode._left) {
        return currentNode._left.getValuesBetweenNodes(
          searchValue,
          currentNode._left,
          valuesArray
        );
      } else {
        return [];
      }
    } else {
      return [];
    }
  }

  sumValuesBetweenNodes(searchValue) {
    const pathArray = this.getValuesBetweenNodes(searchValue);
    if (pathArray) {
      return pathArray.reduce((total, accum) => {
        return total + accum;
      }, 0);
    }
    return pathArray;
  }
}

module.exports = Node;
