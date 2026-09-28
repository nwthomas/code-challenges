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

// Preserve JavaScript's string comparison for legacy callers as well as numeric nodes.
function compareValues(
    left: number | string | null,
    right: number | string | null | undefined,
): number {
    if (typeof left === "string" && typeof right === "string") {
        return left < right ? -1 : left > right ? 1 : 0;
    }
    return Number(left) - Number(right);
}

class Node {
    _value: number | null;
    _left: Node | null;
    _right: Node | null;

    constructor(value: number | null = null) {
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
    getAllValues(node: Node = this) {
        if (node instanceof Node === false) {
            return null;
        }
        const finalValues: number[] = [];
        if (this.getValue() === null) {
            return finalValues;
        }
        function _findValues(_node: Node) {
            finalValues.push(_node.getValue()!);
            _node._left && _findValues(_node._left);
            _node._right && _findValues(_node._right);
        }
        _findValues(node);
        return finalValues;
    }
    findValue(
        searchValue: string | number | undefined = undefined,
        node: Node = this,
    ): boolean | null {
        if (searchValue === undefined || node instanceof Node === false) {
            return null;
        }
        const current = node;
        const currentValue = current.getValue();
        if (currentValue === searchValue) {
            return true;
        } else if (compareValues(currentValue, searchValue) > 0) {
            return current._left
                ? current.findValue(searchValue, current._left)
                : false;
        } else if (compareValues(currentValue, searchValue) < 0) {
            return current._right
                ? current.findValue(searchValue, current._right)
                : false;
        } else {
            return false;
        }
    }
    addValue(
        newValue: number | null | undefined = undefined,
        node: Node = this,
    ): number | Node | boolean | null {
        if (newValue === undefined || node instanceof Node === false) {
            return null;
        }
        const current = node;
        const currentValue = current.getValue();
        if (currentValue === newValue) {
            return newValue;
        } else if (Number(currentValue) > Number(newValue)) {
            if (current._left) {
                return current.addValue(newValue, current._left);
            } else {
                return (current._left = new Node(newValue));
            }
        } else if (Number(currentValue) < Number(newValue)) {
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
    addValueReverse(
        newValue: number | null | undefined = undefined,
        node: Node = this,
    ): number | Node | boolean | null {
        if (newValue === undefined || node instanceof Node === false) {
            return null;
        }
        const current = node;
        const currentValue = current.getValue();
        if (currentValue === newValue) {
            return newValue;
        } else if (Number(currentValue) < Number(newValue)) {
            if (current._left) {
                return current.addValue(newValue, current._left);
            } else {
                return (current._left = new Node(newValue));
            }
        } else if (Number(currentValue) > Number(newValue)) {
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
    _head: Node | null;
    _reversed: Node | null;

    constructor(binaryTreeHead: Node | null = null) {
        this._head = binaryTreeHead;
        this._reversed = null;
    }
    reverse(current: Node | null = this._head): void {
        if (!current) return;
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

export { Node, ReverseBinaryTreeHelper };
