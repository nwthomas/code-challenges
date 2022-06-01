"""
https://leetcode.com/problems/same-tree/

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false
 

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from typing import Optional, TreeNode

def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif p and not q or q and not p:
        return False
    
    tracker = [[p, q]]
    
    while len(tracker):
        one, two = tracker.pop()
        
        if one.val != two.val:
            return False
        
        if one.left and two.left:
            tracker.append([one.left, two.left])
        elif one.left and not two.left or two.left and not one.left:
            return False
        
        if one.right and two.right:
            tracker.append([one.right, two.right])
        elif one.right and not two.right or two.right and not one.right:
            return False
        
    return True