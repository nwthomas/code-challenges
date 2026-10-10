"""
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
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root: TreeNode | None, subRoot: TreeNode | None) -> bool:
    if not root or not subRoot:
        return not root and not subRoot

    def traverse(rootNode: TreeNode | None, subRootNode: TreeNode | None) -> bool:
        queue = [(rootNode, subRootNode)]
        while queue:
            current1, current2 = queue.pop()

            if current1 and not current2:
                return False
            if not current1 and current2:
                return False
            if current1 and current2 and current1.val != current2.val:
                return False

            if current1 and current2:
                queue.extend([(current1.left, current2.left),
                              (current1.right, current2.right)])

        return True

    queue = [root]
    while queue:
        current = queue.pop()

        if current.val == subRoot.val:
            result = traverse(current, subRoot)

            if result:
                return True

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False
