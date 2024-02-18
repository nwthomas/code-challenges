from binary_tree_minimum_sum import Node, find_minumum_level_sum
import unittest
from typing import List

class TestFindMinimumLevelSum(unittest.TestCase):
    def test_find_minimum_level_sum(self):
        """Takes in a tree and returns minimum level sum"""
        root_node = Node(11)
        root_node.left = Node(-10)
        root_node.left.left = Node(6)
        root_node.left.right = Node(5)
        root_node.right = Node(20)
        root_node.right.left = Node(7)
        root_node.right.right = Node(5)

        result = find_minumum_level_sum(root_node)
        self.assertEqual(result, 10)

    def test_finds_minimum_level_in_single_path(self):
        """Takes in a tree with a single path and returns the minimum sum level"""
        root_node = Node(10, Node(9, Node(50, Node(6, Node(-5, Node(400, Node(-90, Node(7))))))))
        result = find_minumum_level_sum(root_node)
        self.assertEqual(result, -90)

if __name__ == "__main__":
    unittest.main()