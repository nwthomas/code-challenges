"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:
Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:
The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

from heapq import heappop, heappush
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    heap = []
    tracker = [root]
    
    while len(tracker) > 0:
        current = tracker.pop()
        
        heappush(heap, current.val)
        
        if current.left:
            tracker.append(current.left)
        if current.right:
            tracker.append(current.right)
            
    current_k = 0
    kth_smallest_val = None
    
    while current_k < k:
        kth_smallest_val = heappop(heap)
        current_k += 1
            
    return kth_smallest_val