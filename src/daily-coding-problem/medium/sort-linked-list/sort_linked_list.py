"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


class Node:
    def __init__(self, value=None, prevNode=None, nextNode=None):
        """
        Constructor for a new Node on the linked list
        """
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

    def addValue(self, value=None):
        """
        Adds a new value to the linked list
        """
        if not value:
            return False
        else:
            current = self
            while current.nextNode:
                current = current.nextNode
            current.nextNode = Node(value, self)
            return True

    def delete(self):
        """
        Deletes a given Node from the linked list and removes references so that it can be
        garbage collected
        """
        value = self.value
        self.prevNode.nextNode = self.nextNode
        self.nextNode.prevNode = self.prevNode
        self.prevNode = None
        self.nextNode = None
        return value

    def insertInFront(self, value):
        """
        Inserts a given value in front of the current Node
        """
        nextNode = self.nextNode
        self.nextNode = Node(value, self, nextNode)
        if nextNode is not None:
            nextNode.prevNode = self.nextNode

    def insertBehind(self, value):
        """
        Inserts a given value bheind the current Node
        """
        prevNode = self.prevNode
        self.prevNode = Node(value, prevNode, self)
        if prevNode is not None:
            prevNode.nextNode = self.prevNode


def sort_doubly_linked_list(dll_list):
    """
    Takes in a doubly-linked list and sorts it in O(n log n) time
    """
    pass
