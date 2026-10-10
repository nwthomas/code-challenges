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


class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


def reverseKGroup(head: ListNode | None, k: int) -> ListNode | None:
    if not head:
        return None

    values = []
    current = head
    while current:
        segment = []

        for _ in range(k):
            if not current:
                break

            segment.append(current.val)
            current = current.next

        values.append(segment)

    newRoot = ListNode()
    current = newRoot
    for v in values:
        currentValues = v

        if len(currentValues) == k:
            currentValues = reversed(currentValues)

        for num in currentValues:
            current.next = ListNode(num)
            current = current.next

    return newRoot.next
