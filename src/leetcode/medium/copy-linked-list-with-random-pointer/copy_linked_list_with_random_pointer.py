"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/

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
"""

from typing import Optional

class Node:
	def __init__(self, val=0, next=None, random=None):
		self.val = val
		self.next = next
		self.random = random

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
	cache = {hex(id(head)): Node(head.val)} if head is not None else {}
	tracker = [head] if head is not None else []

	while len(tracker) > 0:
		current = tracker.pop()
		currentCopy = cache[hex(id(current))]

		if current.next is not None:
			nextNode = cache[hex(id(current.next))] if hex(id(current.next)) in cache else Node(current.next.val)
			cache[hex(id(current.next))] = nextNode
			currentCopy.next = nextNode
			tracker.append(current.next)
		if current.random is not None:
			randomNode = cache[hex(id(current.random))] if hex(id(current.random)) in cache else Node(current.random.val)
			cache[hex(id(current.random))] = randomNode
			currentCopy.random = randomNode

	return cache[hex(id(head))] if head is not None else None