/*
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.

For example, given the following tree and K of 20

    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.
*/

class Node {
    value: number | null;
    left: Node | null;
    right: Node | null;

    constructor(
        value: number | null = null,
        left: Node | null = null,
        right: Node | null = null,
    ) {
        /**
         * Creates a new Node in the Binary Search Tree.
         *
         * @param {number} value The number to be added to a new Node in the tree.
         *
         * @param {Node} left The left Node reference in the Binary Search Tree from the current
         * Node.
         *
         * @param {Node} right The right Node reference in the Binary Search Tree from the current
         * Node.
         */
        this.value = value;
        this.left = left;
        this.right = right;
    }

    addValue(value: number, current: Node = this) {
        /**
         * Adds a new value to the Binary Search Tree
         *
         * @param {number} value The number to be added to a new Node in the tree.
         *
         * @param {Node} current This parameter is mainly used internally to recursively call
         * the function until the correct spot is found to add the value.
         */
        if (!current.value) {
            current.value = value;
        } else {
            if (Number(value) >= current.value) {
                if (current.right) {
                    current.addValue(value, current.right);
                } else {
                    current.right = new Node(value);
                }
            }
            if (Number(value) < current.value) {
                if (current.left) {
                    current.addValue(value, current.left);
                } else {
                    current.left = new Node(value);
                }
            }
        }
    }
}

function findSumInBinaryTree(rootNode: string | Node, k: string | number) {
    /**
     * Takes in a root Node for a Binary Search Tree and a number (k). If there are two Nodes in
     * the tree that add up to the number k, then those two Nodes are returned. If no two Nodes
     * add up to the number k, an empty array is returned.
     *
     * @param {Node} rootNode The root, initial Node of a Binary Search Tree of integers.
     *
     * @param {number} k A number that two Nodes should add up to.
     *
     * @returns {array} Returns an array of two Nodes if they add up to k or otherwise an empty array.
     */
    if (rootNode instanceof Node !== true || typeof k !== "number") {
        return [];
    }
    const tracker: Record<number, Node> = {};
    const queue = [rootNode];
    while (queue.length) {
        const currentNode = queue.shift()!;
        if (!tracker[Number(currentNode.value)]) {
            tracker[Number(currentNode.value)] = currentNode;
        }
        if (tracker[k - Number(currentNode.value)]) {
            return [tracker[k - Number(currentNode.value)], currentNode];
        }
        if (currentNode.left) {
            queue.push(currentNode.left);
        }
        if (currentNode.right) {
            queue.push(currentNode.right);
        }
    }
    return [];
}

export { findSumInBinaryTree, Node };
