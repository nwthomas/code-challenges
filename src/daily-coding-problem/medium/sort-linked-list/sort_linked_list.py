from copy import deepcopy

"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a linked list, sort it in O(n log n) time and constant space.

For example, the linked list 4 -> 1 -> -3 -> 99 should become -3 -> 1 -> 4 -> 99.
"""


class DoublyLinkedList:
    def __init__(self, value=None):
        """
        Constructor for instantiating a new Doubly-Linked List
        """
        self.head = Node(value) if value else None
        self.tail = self.head if self.head else None
        self.length = 1 if value else 0

    def add_value(self, new_value=None):
        """
        Adds a new value to the Doubly-Linked List
        """
        if new_value:
            if self.head:
                current = self.head
                while current.next_node:
                    current = current.next_node
                current.next_node = Node(new_value)
                current.next_node.prev_node = current
                self.length += 1
                return True
            elif not self.head:
                self.head = Node(new_value)
                self.length += 1
                return True
            else:
                return False
        else:
            return False

    def sort_list(self):
        """
        Sorts the Doubly-Linked List in O(n log n) with constant space complexity
        """
        start = self.head
        end = self.tail
        for _ in range(0, self.length // 2):
            self._sort_range_of_list(start, end)
            start = start.next_node
            end = end.prev_node

    def _sort_range_of_list(self, head, tail):
        """
        Private method for finding the biggest and smallest values between head and tail and
        swapping those values with the input head and tail arguments
        """
        start = head
        end = tail
        replacement_start = None
        replacement_end = None
        current_left = head
        current_right = tail
        while current_left.prev_node != current_right or current_left != current_right:
            if current_left.value < start.value:
                if not replacement_start or current_left.value < replacement_start.value:
                    replacement_start = current_left
            if current_right.value > end.value:
                if not replacement_end or current_right.value > replacement_end.value:
                    replacement_end = current_right
        if replacement_start:
            temp = start.value
            start.value = replacement_start.value
            replacement_start.value = temp
        if replacement_end:
            temp = end.value
            end.value = replacement_end.value
            replacement_end.value = temp


class Node:
    def __init__(self, value=None, prev_node=None, next_node=None):
        """
        Constructor for a new Node on the linked list
        """
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def add_value(self, new_value=None):
        """
        Adds a new value to the linked list
        """
        if not new_value:
            return False
        else:
            if not self.value:
                self.value = new_value
            else:
                current = self
                while current.next_node:
                    current = current.next_node
                current.next_node = Node(new_value, self)
            return True

    def delete(self):
        """
        Deletes a given Node from the linked list and removes references so that it can be
        garbage collected
        """
        value = self.value
        if self.prev_node:
            self.prev_node.next_node = self.next_node
        if self.next_node:
            self.next_node.prev_node = self.prev_node
        self.prev_node = None
        self.next_node = None
        return value
