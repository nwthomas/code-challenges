"""
Good morning! Here's your coding interview problem for today.

This problem was asked by LinkedIn.

Determine whether a tree is a valid binary search tree.

A binary search tree is a tree with two children, left and right, and satisfies the constraint that the key in the left child must be less than or equal to the root and the key in the right child must be greater than or equal to the root.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def add_value_to_tree(self, value):
        current_node = self.root
        is_searching = True

        while is_searching:
            if current_node.value < value and current_node.right:
                current_node = current_node.right
            elif current_node.value < value:
                current_node.right = Node(value)
                is_searching = False
            elif current_node.value >= value and current_node.left:
                current_node = current_node.left
            elif current_node.value >= value:
                current_node.left = Node(value)
                is_searching = False
            else:
                is_searching = False

def is_valid_binary_search_tree(bst):
    """Takes in a Binary Search Tree and returns True if valid and False if not"""
    node_stack = [bst.root]

    while len(node_stack) >= 1:
        current_node = node_stack.pop()

        if current_node.left and current_node.value >= current_node.left.value:
            node_stack.append(current_node.left)
        elif current_node.left:
            return False

        if current_node.right and current_node.value < current_node.right.value:
            node_stack.append(current_node.right)
        elif current_node.right:
            return False

    return True

