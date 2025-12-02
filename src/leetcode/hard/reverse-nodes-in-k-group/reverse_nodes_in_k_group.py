"""
https://leetcode.com/problems/reverse-nodes-in-k-group

You are given the head of a singly linked list head and a positive integer k.

You must reverse the first k nodes in the linked list, and then reverse the next k nodes, and so on. If there are fewer than k nodes left, leave the nodes as they are.

Return the modified list after reversing the nodes in each group of k.

You are only allowed to modify the nodes' next pointers, not the values of the nodes.

Example 1:
Input: head = [1,2,3,4,5,6], k = 3
Output: [3,2,1,6,5,4]

Example 2:
Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]

Constraints:
The length of the linked list is n.
1 <= k <= n <= 100
0 <= Node.val <= 100
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    lists = [[head]] if head is not None else head
    if len(lists) > 0:
        head = head.next

    while head:
        if len(lists[len(lists) - 1]) == k:
            lists.append([])

        temp = head.next
        lists[len(lists) - 1].append(head)
        head = temp

    for i, group in enumerate(lists):
        if len(group) == k:
            for j, node in enumerate(group):
                node.next = None
                if j > 0:
                    node.next = group[j - 1]

            if i > 0:
                lists[i - 1][0].next = group[len(group) - 1]
        else:
            if i > 0:
                lists[i - 1][0].next = group[0]

    return lists[0][len(lists[0]) - 1] if len(lists) > 0 else None
