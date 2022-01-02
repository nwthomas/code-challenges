"""
Delete a node from a singly-linked list, ↴ given only a variable pointing to that node.

The input could, for example, be the variable b below:

class LinkedListNode(object):

def __init__(self, value):
    self.value = value
    self.next  = None

a = LinkedListNode('A')
b = LinkedListNode('B')
c = LinkedListNode('C')

a.next = b
b.next = c

delete_node(b)
"""

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add_node_to_list(self, value):
        """Adds a new node to the SLL"""
        if not self.head:
            self.head = Node(value)
        else:
            current = self.head

            while current.next:
                current = current.next
            
            current.next = Node(value)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def delete_node(node):
    """Takes in a node and deletes it from a chain where it is not the end node"""
    next_node = node.next
    node.value = next_node.value
    node.next = next_node.next

    # Allows garbage collection of node with no reference/use
    next_node.next = None




