"""
https://leetcode.com/problems/merge-k-sorted-lists/

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]

Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""

from heapq import heappop, heappush
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    tracker = [root_node for root_node in lists]
    
    while len(tracker):
        current_node = tracker.pop()
        
        if not current_node:
            continue
        
        heappush(heap, current_node.val)
        
        if current_node.next:
            tracker.append(current_node.next)
            
    root = ListNode(heappop(heap)) if len(heap) > 0 else None
    current = root if root else None
    
    while current and len(heap) > 0:
        current_value = heappop(heap)
        
        current.next = ListNode(current_value)
        current = current.next
        
    return root