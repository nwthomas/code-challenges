/*
https://leetcode.com/problems/balanced-binary-tree

Given a binary tree, return true if it is height-balanced and false otherwise.

A height-balanced binary tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:
Input: root = [1,2,3,null,null,4]
Output: true

Example 2:
Input: root = [1,2,3,null,null,4,null,5]
Output: false

Example 3:
Input: root = []\
Output: true

Constraints:
The number of nodes in the tree is in the range [0, 1000].
-1000 <= Node.val <= 1000
*/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function isBalanced(root) {
    function traverse(node) {
        if (!node) {
            return [true, 0];
        }

        const left = traverse(node.left);
        const right = traverse(node.right);
        const balanced =
            left[0] && right[0] && Math.abs(left[1] - right[1]) <= 1;

        return [balanced, 1 + Math.max(left[1], right[1])];
    }

    return traverse(root)[0];
}

module.exports = { isBalanced, TreeNode };
