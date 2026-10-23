"""
https://leetcode.com/problems/reorder-list/

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

Constraints:
The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def reorder_list(head: Optional[ListNode]):
    """]
    :type head: Optional[ListNode]
    :rtype: None Do not return anything, modify head in-place instead.
    """
    l = []

    current = head
    while current:
        nextCurrent = current.next
        current.next = None
        l.append(current)
        current = nextCurrent

    if len(l) <= 1:
        return l[0] if l else None

    left = 0
    right = len(l) - 1
    dummyHead = ListNode()
    current = dummyHead
    while left < right:
        nodeOne = l[left]
        nodeTwo = l[right]
        current.next = nodeOne
        current.next.next = nodeTwo
        current = current.next.next
        left += 1
        right -= 1

    if len(l) % 2 != 0:
        current.next = l[left]

    head = dummyHead.next
    dummyHead.next = None

    return head
