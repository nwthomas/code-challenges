"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given a binary tree and an integer k, return whether there exists a root-to-leaf path that sums up to k.

For example, given k = 18 and the following binary tree:

    8
   / \
  4   13
 / \   \
2   6   19

Return True since the path 8 -> 4 -> 6 sums to 18.
"""


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_value(self, value):
        """Takes in a value and adds it to the binary tree"""
        if not self.root:
            self.root = Node(value)
        else:
            current = self.root
            next_value = self.get_next_node(current, value)

            while next_value:
                current = next_value
                next_value = self.get_next_node(current, value)

            if value >= current.value:
                current.right = Node(value)
            else:
                current.left = Node(value)

    def get_next_node(self, node, next_value):
        """Compares a node to a value and returns the direction the binary tree should go"""
        return node.right if next_value >= node.right else node.left

    def find_if_sum_exists(self, total):
        """Checks if the sume of a total exists in the tree paths and returns True or False otherwise"""
        tracker = [(self.root, self.root.value)]

        while len(tracker) > 0:
            current = tracker.pop()

            right_node = current[0].right
            left_node = current[0].left

            if right_node:
                right_value = right_node.value
                new_total = current[1] + right_value

                if new_total == total:
                    return True
                else:
                    tracker.append((right_node, new_total))

            if left_node:
                left_value = left_node.value
                new_total = current[1] + left_value

                if new_total == total:
                    return True
                else:
                    tracker.append((left_node, new_total))

        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def add_value(self, node):
        """Takes in a node and adds it to the left or right"""
        if node.value >= self.value:
            self.right = node
        else:
            self.left = node
