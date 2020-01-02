"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Determine whether a doubly linked list is a palindrome. What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.
"""


class Node:
    def __init__(self, value=None, next_value=None):
        self._value = value
        self._next = next_value

    def add_value(self, value=None):
        """
        Adds a new value to the end of the linked list

        Returns a True boolean if added or else False
        """
        current = self
        if current._value:
            while current._next:
                current = current._next
            current._next = Node(value)
            return True
        else:
            if current._value == None:
                current._value = value
                return True
            else:
                return False

    def get_list_values(self):
        """
        Returns all values from this Node through to the end
        """
        l_value = []
        current = self
        while current:
            l_value.append(current._value)
            current = current._next
        return l_value


def is_palindrome(l):
    l_string = ""
    l_string_reversed = ""
    for val in l:
        l_string = l_string + f"{val}"
    for val in reversed(l_string):
        l_string_reversed = l_string_reversed + f"{val}"
    if l_string == l_string_reversed:
        return True
    else:
        return False
