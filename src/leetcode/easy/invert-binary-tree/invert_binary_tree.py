"""
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree, and return its root.

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """Takes in a Tree and inverts it by swapping the left and right nodes of each node"""

    def invert(node: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return
        
        temp_right = node.right
        node.right = invert(node.left)
        node.left = invert(temp_right)

        return node
    
    return invert(root)