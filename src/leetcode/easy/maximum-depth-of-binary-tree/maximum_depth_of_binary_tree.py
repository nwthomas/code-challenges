"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: Optional[TreeNode]) -> int:
    max_depth = 0
    tracker = [[root, 1]] if root else []
    
    while len(tracker) > 0:
        current, depth = tracker.pop()
        
        if depth > max_depth:
            max_depth = depth
        
        if current.left:
            tracker.append([current.left, depth + 1])
        
        if current.right:
            tracker.append([current.right, depth + 1])
    
    return max_depth