"""
https://leetcode.com/problems/binary-tree-level-order-traversal/

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    tracker = deque()
    result = []
    
    if root:
        tracker.append([root, 0])
    
    while len(tracker) > 0:
        node, level = tracker.pop()
        
        if len(result) <= level:
            result.append([])
            
        result[level].append(node.val)
        
        if node.left:
            tracker.appendleft([node.left, level + 1])
        
        if node.right:
            tracker.appendleft([node.right, level + 1])
            
    return result