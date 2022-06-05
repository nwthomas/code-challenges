"""
https://leetcode.com/problems/merge-two-sorted-lists/

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]

Constraints:
The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    new_head = None
    new_current = None
    current_list1 = list1
    current_list2 = list2
    
    if not list1 and not list2:
        return new_head
    
    def add_value(val):
        nonlocal new_head
        nonlocal new_current
        
        if not new_head:
            new_head = ListNode(val)
            new_current = new_head
        else:
            new_current.next = ListNode(val)
            new_current = new_current.next
    
    while current_list1 or current_list2:
        if current_list1 and current_list2 and current_list1.val <= current_list2.val:
            new_value = current_list1.val
            add_value(new_value)
            current_list1 = current_list1.next
        elif current_list1 and current_list2:
            new_value = current_list2.val
            add_value(new_value)
            current_list2 = current_list2.next
        elif current_list1:
            new_value = current_list1.val
            add_value(new_value)
            current_list1 = current_list1.next
        else:
            new_value = current_list2.val
            add_value(new_value)
            current_list2 = current_list2.next
            
    return new_head