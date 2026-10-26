/*
https://leetcode.com/problems/serialize-and-deserialize-binary-tree

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Example 1:
Input: root = [1,2,3,null,null,4,5]
Output: [1,2,3,null,null,4,5]

Example 2:
Input: root = []
Output: []
 
Constraints:
The number of nodes in the tree is in the range [0, 104].
-1000 <= Node.val <= 1000
*/

type JSONValue = {
    val: number;
    left: JSONValue | null;
    right: JSONValue | null;
};

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val === undefined ? 0 : val;
        this.left = left === undefined ? null : left;
        this.right = right === undefined ? null : right;
    }
}

export function serialize(root: TreeNode | null): string {
    function buildJson(node: TreeNode | null): JSONValue | null {
        if (!node) {
            return null;
        }

        const currentNode = {
            val: node.val,
            left: buildJson(node.left),
            right: buildJson(node.right),
        };

        return currentNode;
    }

    const json = root ? buildJson(root) : { val: null };

    return JSON.stringify(json);
}

export function deserialize(data: string): TreeNode | null {
    const json = JSON.parse(data);

    function buildTree(node: JSONValue | null): TreeNode | null {
        if (!node?.val && node?.val !== 0) {
            return null;
        }

        const newNode = new TreeNode(node.val);
        if (node.left) {
            newNode.left = buildTree(node.left);
        }
        if (node.right) {
            newNode.right = buildTree(node.right);
        }

        return newNode;
    }

    return buildTree(json);
}
