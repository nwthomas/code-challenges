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
            previous = self.root
            current = self.root.right if value >= self.root.value else self.root.left

            while current:
                previous = current
                current = current.right if value >= current.value else current.left

            if value >= previous.value:
                previous.right = Node(value)
            else:
                previous.left = Node(value)

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
