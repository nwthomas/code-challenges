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
    inverted_root = TreeNode(root.val) if root else None
    tracker = [[root, inverted_root]] if root else []
    
    while len(tracker) > 0:
        original_current, new_current = tracker.pop()
        
        if original_current.right:
            new_current.left = TreeNode(original_current.right.val)
            tracker.append([original_current.right, new_current.left])
        
        if original_current.left:
            new_current.right = TreeNode(original_current.left.val)
            tracker.append([original_current.left, new_current.right])
            
    return inverted_root