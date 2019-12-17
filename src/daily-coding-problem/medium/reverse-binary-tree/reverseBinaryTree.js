/*

Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Invert a binary tree.

For example, given the following tree:

    a
   / \
  b   c
 / \  /
d   e f
should become:

  a
 / \
 c  b
 \  / \
  f e  d

*/

class Node {
  constructor(value = null) {
    this._value = value;
    this._left = null;
    this._right = null;
  }
  getTree() {
    return JSON.stringify(this);
  }
  getValue() {
    return this._value;
  }
  getAllValues(node = this) {
    if (node instanceof Node === false) {
      return null;
    }
    const finalValues = [];
    if (this.getValue() === null) {
      return finalValues;
    }
    function _findValues(_node) {
      finalValues.push(_node.getValue());
      _node._left && _findValues(_node._left);
      _node._right && _findValues(_node._right);
    }
    _findValues(node);
    return finalValues;
  }
  findValue(searchValue, node = this) {
    if (searchValue === undefined || node instanceof Node === false) {
      return null;
    }
    const current = node;
    const currentValue = current.getValue();
    if (currentValue === searchValue) {
      return true;
    } else if (currentValue > searchValue) {
      return current._left
        ? current.findValue(searchValue, current._left)
        : false;
    } else if (currentValue < searchValue) {
      return current._right
        ? current.findValue(searchValue, current._right)
        : false;
    } else {
      return false;
    }
  }
  addValue(newValue, node = this) {
    if (newValue === undefined || node instanceof Node === false) {
      return null;
    }
    const current = node;
    const currentValue = current.getValue();
    if (currentValue === newValue) {
      return newValue;
    } else if (currentValue > newValue) {
      if (current._left) {
        return current.addValue(newValue, current._left);
      } else {
        return (current._left = new Node(newValue));
      }
    } else if (currentValue < newValue) {
      if (current._right) {
        return current.addValue(newValue, current._right);
      } else {
        current._right = new Node(newValue);
        return newValue;
      }
    } else {
      return false;
    }
  }
  addValueReverse(newValue, node = this) {
    if (newValue === undefined || node instanceof Node === false) {
      return null;
    }
    const current = node;
    const currentValue = current.getValue();
    if (currentValue === newValue) {
      return newValue;
    } else if (currentValue < newValue) {
      if (current._left) {
        return current.addValue(newValue, current._left);
      } else {
        return (current._left = new Node(newValue));
      }
    } else if (currentValue > newValue) {
      if (current._right) {
        return current.addValue(newValue, current._right);
      } else {
        current._right = new Node(newValue);
        return newValue;
      }
    } else {
      return false;
    }
  }
}

class ReverseBinaryTreeHelper {
  constructor(binaryTreeHead = null) {
    this._head = binaryTreeHead;
    this._reversed = null;
  }
  reverse(current = this._head) {
    if (!this._reversed) {
      this._reversed = new Node(current.getValue());
    } else {
      this._reversed.addValueReverse(current.getValue());
    }
    if (current._left) {
      this.reverse(current._left);
    }
    if (current._right) {
      this.reverse(current._right);
    }
  }
  getReversedHead() {
    return JSON.stringify(this._reversed);
  }
}

module.exports = { Node, ReverseBinaryTreeHelper };
