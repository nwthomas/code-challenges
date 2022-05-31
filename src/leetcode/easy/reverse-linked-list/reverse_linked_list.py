"""
https://leetcode.com/problems/reverse-linked-list/

Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
"""

from typing import ListNode, Optional

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None
    
    prev_node = None
    current_node = head
    next_node = current_node.next
    
    current_node.next = prev_node
    
    while next_node:
        prev_node = current_node
        current_node = next_node
        next_node = current_node.next
        current_node.next = prev_node
        
    return current_node