/*
https://leetcode.com/problems/diameter-of-binary-tree/

Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.
The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1
 
Constraints:
The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
*/

class TreeNode {
    constructor(val = 0, left = null, right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

const traverse = (node) => {
    if (!node) {
        return { longestCombined: 0, longestCurrent: 0 };
    }

    let leftResults = traverse(node.left);
    let rightResults = traverse(node.right);
    const longestCurrent = (leftResults.longestCurrent > rightResults.longestCurrent ? leftResults.longestCurrent : rightResults.longestCurrent) + 1;
    let longestCombined = leftResults.longestCurrent + rightResults.longestCurrent + 1;
    if (leftResults.longestCombined > longestCombined) {
        longestCombined = leftResults.longestCombined;
    }
    if (rightResults.longestCombined > longestCombined) {
        longestCombined = rightResults.longestCombined;
    }

    return { longestCombined, longestCurrent };
}

const diameterOfBinaryTree = (root) => {
    const result = traverse(root);

    // The traverse function calculates vertices, and we want edges. Simplest way is just to -1
    // before returning the final result from the function.
    return result.longestCombined - 1;
}

module.exports = { diameterOfBinaryTree, TreeNode };