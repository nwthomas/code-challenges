"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def get_binary_tree_paths(root_node: TreeNode):
    paths = []
    stack = [[root_node, [root_node.value]]]

    while len(stack) > 0:
        current_node, path = stack.pop()

        if current_node.left or current_node.right:
            if current_node.left:
                stack.append([current_node.left, path + [current_node.left.value]])
            if current_node.right:
                stack.append([current_node.right, path + [current_node.right.value]])
        elif len(path) > 0:
            paths.append(path)

    return paths