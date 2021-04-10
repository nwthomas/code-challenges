"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.
"""
from random import randrange

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_node(self, value):
        """Adds a value to the singly linked list"""
        current = self

        while current.next:
            current = current.next

        current.next = Node(value)

def get_singly_linked_list_nodes(*args):
    """connects any number of singly linked lists together"""
    node_dict = {}
    values_list = []

    def add_node_to_dict(node):
        if node.value in node_dict:
            node_dict[node.value].append(node)
        else:
            node_dict[node.value] = [node]

        values_list.append(node.value)

    for node in args:
        add_node_to_dict(node)
        current_node = node

        while current_node.next:
            # We need to clear the next reference to avoid an infinite loop when joined later
            temp = current_node.next
            current_node.next = None
            current_node = temp
            add_node_to_dict(current_node)

    return (node_dict, values_list)

def quick_sort_singly_linked_lists(unsorted_node_dict, values_list):
    """Quick sorts a group of nodes with an associated values list"""
    if len(values_list) == 1:
        return [node for node in unsorted_node_dict[values_list[0]]]
    elif len(values_list) < 1:
        return []
    elif values_list:
        random_index = randrange(len(values_list))
        pivot_value = values_list[random_index]

        lower_nodes = {}
        lower_values = []

        equal_nodes = []

        higher_nodes = {}
        higher_values = []

        for value in values_list:
            # This covers cases where we've already removed multiple of the same integer
            # from the dict and removed with the delete keyword
            if not value in unsorted_node_dict:
                continue
            else:
                if value > pivot_value:
                    higher_nodes[value] = unsorted_node_dict[value]
                    del unsorted_node_dict[value]
                    higher_values.append(value)
                elif value < pivot_value:
                    lower_nodes[value] = unsorted_node_dict[value]
                    del unsorted_node_dict[value]
                    lower_values.append(value)
                else:
                    equal_nodes += [node for node in unsorted_node_dict[value]]
    
        return quick_sort_singly_linked_lists(lower_nodes, lower_values) + equal_nodes + quick_sort_singly_linked_lists(higher_nodes, higher_values)

def join_sorted_node_list(sorted_node_list):
    """Takes in a sorted node list and returns a sorted singly linked list"""
    head_node = None
    current_node = None

    for node in sorted_node_list:
        if not head_node:
            head_node = node
            current_node = head_node
        else:
            current_node.next = node
            current_node = current_node.next
    
    return head_node

def sort_singly_linked_lists(*args):
    """Takes in any number of sorted Singly Linked Lists and returns one that is sorted"""
    unsorted_node_dict, unsorted_values_list = get_singly_linked_list_nodes(*args)
    sorted_node_list = quick_sort_singly_linked_lists(unsorted_node_dict, values_list=unsorted_values_list)
    sorted_singly_linked_list = join_sorted_node_list(sorted_node_list)

    return sorted_singly_linked_list

