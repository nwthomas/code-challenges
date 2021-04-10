"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""
from random import randrange

class SinglyLinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    
    def add_node(self, value):
        """Adds a value to the singly linked list"""
        current = self.head

        while current.next:
            current = current.next

        current.next = Node(value)
        self.tail = current.next
        self.length += 1

class Node:
    def __init__(self, value, next_value = None):
        self.value = value
        self.next = next_value

    def __str__(self):
        node_string = f"{self.value}"
        return f"{node_string} --> {self.next}" if self.next else node_string

def connect_singly_linked_lists(*args):
    """connects any number of singly linked lists together"""
    final_list = None

    for next_list in args:
        if not final_list:
            final_list = next_list
        else:
            final_list.tail.next = next_list.head
            final_list.tail = next_list.tail
            final_list.length += next_list.length

            # Remove all references from old list class for garbage collection
            next_list.head = None
            next_list.tail = None

    return final_list


def quick_sort_singly_linked_lists(*args):
    """Takes in any number of sorted Singly Linked Lists and returns one that is sorted"""
    unsorted_list = connect_singly_linked_lists(*args)

    return unsorted_list

