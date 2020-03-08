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
        if not new_value:
            return False
        elif self.tail:
            isAdded = self.tail.add_value(new_value)
            self.tail = self.tail.next_node
            return isAdded
        else:
            self.head = Node(new_value)
            self.tail = self.head

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

    def _sort_range_of_list(self, head=None, tail=None):
        """
        Private method for finding the biggest and smallest values between head and tail and
        swapping those values with the input head and tail arguments
        """
        replacement_head = head
        replacement_tail = tail
        current_left = head
        current_right = tail
        while current_left != current_right and current_left and current_right and (current_left.prev_node != current_right):
            if current_left.value < head.value or current_right.value < head.value or current_right.value > tail.value or current_left.value > head.value:
                if current_left.value < replacement_head.value:
                    replacement_head = current_left
                if current_right.value < replacement_head.value:
                    replacement_head = current_right
                if current_left.value > replacement_tail.value:
                    replacement_tail = current_left
                if current_right.value > replacement_tail.value:
                    replacement_tail = current_right
            current_left = current_left.next_node
            current_right = current_right.prev_node
        if replacement_tail == replacement_head and replacement_head and replacement_tail:
            temp = replacement_head.value
            replacement_head.value = replacement_tail.value
            replacement_tail.value = temp
        else:
            if replacement_head:
                temp = head.value
                head.value = replacement_head.value
                replacement_head.value = temp
            if replacement_tail:
                temp = tail.value
                tail.value = replacement_tail.value
                replacement_tail.value = temp


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
                current.next_node = Node(new_value, current)
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
