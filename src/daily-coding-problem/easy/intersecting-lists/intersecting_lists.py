"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""

class Node:
    def __init__(self, value, next_value = None):
        self.value = value
        self.next = next_value

class SinglyLinkedList:
    def __init__(self, first_value):
        self.head = None
        self.tail = None
        self.length = 0

        if first_value:
            self.head = Node(first_value)
            self.tail = self.head
            self.length = 1
    
    def add_value(self, value):
        if not self.head:
            self.head = Node(value)
            self.tail = self.head
        else:
            current = self.head

            while current.next:
                current = current.next

            current.next = Node(value)
            self.length = 1
            self.tail = current.next
        
    def __str__(self):
        string = f"(START) {self.head.value}"

        current = self.head.next

        while current:
            string += f" --> {current.value}"
            current = current.next

        return string + " (END)"

def get_intersection_of_lists(list_1, list_2):
    """Takes in two singly-linked lists and returns the intersection of them"""
    longest_list = list_1 if list_1.length > list_2.length else list_2
    shortest_list = list_2 if list_1.length > list_2.length else list_1

    remaining_longest_nodes = longest_list.length

    current_longest_node = longest_list.head
    current_shortest_node = shortest_list.head

    while current_longest_node:
        if remaining_longest_nodes > shortest_list.length:
            current_longest_node = current_longest_node.next
            remaining_longest_nodes -= 1
        else:
            if current_longest_node is current_shortest_node:
                return current_longest_node
            else:
                current_longest_node = current_longest_node.next
                current_shortest_node = current_shortest_node.next