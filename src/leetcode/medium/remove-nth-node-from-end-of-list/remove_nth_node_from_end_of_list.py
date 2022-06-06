"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy_node = ListNode(None, head)
    left = dummy_node
    right = head
    
    while right and n > 0:
        right = right.next
        n -= 1
        
    while right:
        left = left.next
        right = right.next
    
    new_next = left.next.next
    left.next.next = None
    left.next = new_next
    final_head = dummy_node.next
    dummy_node.next = None
    
    return final_head