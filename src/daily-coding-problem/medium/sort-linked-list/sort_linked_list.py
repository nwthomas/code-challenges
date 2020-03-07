"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


class DoublyLinkedList:
    def __init__(self, value=None):
        """
        Constructor for instantiating a new Doubly Linked List
        """
        self.dll_list = Node(value) if value else None
        self.length = 1 if value else 0

    def add_value(self, value=None):
        """
        Adds a new value to the Doubly Linked List
        """
        if value:
            if self.dll_list:
                current = self.dll_list
                while current.nextNode:
                    current = current.nextNode
                current.nextNode = Node(value)
                current.nextNode.prevNode = current
                self.length += 1
                return True
            elif self.dll_list is None:
                self.dll_list = Node(value)
                self.length += 1
                return True
            else:
                return False
        else:
            return False


class Node:
    def __init__(self, value=None, prevNode=None, nextNode=None):
        """
        Constructor for a new Node on the linked list
        """
        self.value = value
        self.prevNode = prevNode
        self.nextNode = nextNode

    def add_value(self, value=None):
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
        if self.prevNode:
            self.prevNode.nextNode = self.nextNode
        if self.nextNode:
            self.nextNode.prevNode = self.prevNode
        self.prevNode = None
        self.nextNode = None
        return value

    def insert_in_front(self, value=None):
        """
        Inserts a given value in front of the current Node
        """
        nextNode = self.nextNode
        self.nextNode = Node(value, self, nextNode)
        if nextNode is not None:
            nextNode.prevNode = self.nextNode

    def insert_behind(self, value):
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


def merge_in_place(listOne, listTwo):
    """
    Takes in two lists and merges them together in 
    """
    pass
