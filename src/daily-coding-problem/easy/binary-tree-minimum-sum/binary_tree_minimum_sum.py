"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return the level of the tree with minimum sum.
"""

class Node:
    def __init__(self, value: int, left: "Node" = None, right: "Node" = None):
        self.value = value
        self.left = left
        self.right = right

def find_minumum_level_sum(tree_root_node: Node) -> int:
    level_sums = {}
    tracker = [[tree_root_node, 0]]

    while len(tracker) > 0:
        current_node, current_level = tracker.pop(0)

        if not current_level in level_sums:
            level_sums[current_level] = 0

        level_sums[current_level] += current_node.value

        if current_node.left:
            tracker.append([current_node.left, current_level + 1])
        if current_node.right:
            tracker.append([current_node.right, current_level + 1])

    minimum_level_sum = float("inf")
    for key in level_sums:
        if level_sums[key] < minimum_level_sum:
            minimum_level_sum = level_sums[key]

    return minimum_level_sum
        


