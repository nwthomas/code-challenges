/*
https://leetcode.com/problems/subtree-of-another-tree

Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.

Example 1:
Input: root = [1,2,3,4,5], subRoot = [2,4,5]
Output: true

Example 2:
Input: root = [1,2,3,4,5,null,null,6], subRoot = [2,4,5]
Output: false

Constraints:
1 <= The number of nodes in both trees <= 100.
-100 <= root.val, subRoot.val <= 100
*/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

const isSameTree = (node1, node2) => {
    if (!node1 && !node2) {
        return true;
    } else if (!node1 || !node2) {
        return false;
    }

    const hasSameVal = node1.val === node2.val;
    if (!hasSameVal) {
        return false;
    }

    const leftResult = isSameTree(node1.left, node2.left);
    const rightResult = isSameTree(node1.right, node2.right);

    return leftResult && rightResult;
};

const isSubtree = (root, subRoot) => {
    if (!root) {
        return !subRoot;
    }
    if (!subRoot) {
        return !root;
    }

    const stack = [];
    if (root) {
        stack.push(root);
    }

    while (stack.length > 0) {
        const currentNode = stack.pop();

        if (currentNode.val === subRoot.val) {
            const result = isSameTree(currentNode, subRoot);

            if (result) {
                return true;
            }
        }

        if (currentNode.left) {
            stack.push(currentNode.left);
        }
        if (currentNode.right) {
            stack.push(currentNode.right);
        }
    }

    return false;
};

module.exports = { isSubtree, TreeNode };
