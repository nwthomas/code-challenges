"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Let's represent an integer in a linked list format by having each node represent a digit in the
number. The nodes make up the number in reversed order.

For example, the following linked list:

1 -> 2 -> 3 -> 4 -> 5
is the number 54321.

Given two linked lists in this format, return their sum in the same linked list format.

For example, given

9 -> 9
5 -> 2
return 124 (99 + 25) as:

4 -> 2 -> 1
"""


class Node:
    def __init__(self, value=None, nextNode=None):
        self._value = value
        self._next = nextNode

    def add_value(self, value=None, current=None):
        """
        Adds a new value to the linked list
        """
        if current == None:
            current = self
        if type(value) != int:
            return False
        else:
            if current._value == None:
                current._value = value
                return True
            if current._next:
                return current.add_value(value, current._next)
            else:
                current._next = Node(value)
                return True


def sum_reversed_lists(root_node_1, root_node_2):
    """
    Takes in two singly-linked lists that store the integers of a number (one per Node) in reversed
    format and return the sum of both lists in a singly-linked list in reversed format.
    """
    num_1 = ""
    num_2 = ""
    current_1 = root_node_1
    current_2 = root_node_2

    while current_1 or current_2:
        if current_1._value:
            num_1 += str(current_1._value)
            current_1 = current_1._next
        if current_2._value:
            num_2 += str(current_1._value)
            current_2 = current_2._next

    num_1_rev = num_1.split().reverse().join()
    num_2_rev = num_2.split().reverse().join()
    total = int(num_1_rev) + int(num_2_rev)
    total_str = str(total)
    new_root_node = Node(total_str[-1])

    for i in range(len(total_str) - 1, -1):
        new_root_node.add_value(total_str[i])

    return new_root_node
