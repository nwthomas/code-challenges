/*

Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.

*/

class Node {
    _value: number | null;
    _left: Node | null;
    _right: Node | null;

    constructor(
        value: number | null = null,
        left: Node | null = null,
        right: Node | null = null,
    ) {
        this._value = value;
        this._left = left;
        this._right = right;
    }
    getValue() {
        return this._value && this._value;
    }
    getAllTreeValues(node: Node = this): (number | null)[] {
        const values = [node.getValue()];
        if (node._left) {
            values.unshift(...this.getAllTreeValues(node._left));
        }
        if (node._right) {
            values.push(...this.getAllTreeValues(node._right));
        }
        return values;
    }
    addValue(
        value: number | null | undefined,
        node: Node = this,
    ): boolean | null {
        if (typeof value === "undefined" || node instanceof Node === false) {
            return null;
        }
        if (!node._value) {
            node._value = value;
            return true;
        }
        if (node.getValue() === value) {
            return true;
        } else if (Number(node.getValue()) > Number(value)) {
            if (node._left) {
                return node.addValue(value, node._left);
            } else {
                node._left = new Node(value);
                return true;
            }
        } else if (Number(node.getValue()) < Number(value)) {
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
    validateTree(node: Node = this): boolean | null | undefined {
        if (node instanceof Node === false) {
            return null;
        }
        if (
            node._right &&
            Number(node._right.getValue()) < Number(node.getValue())
        ) {
            return false;
        }
        if (
            node._left &&
            Number(node._left.getValue()) > Number(node.getValue())
        ) {
            return false;
        }
        if (!node._left && !node._right) {
            return true;
        }
        if (
            node._right &&
            Number(node._right.getValue()) > Number(node.getValue())
        ) {
            return this.validateTree(node._right);
        }
        if (
            node._left &&
            Number(node._left.getValue()) < Number(node.getValue())
        ) {
            return this.validateTree(node._left);
        }
    }
}

export default Node;
