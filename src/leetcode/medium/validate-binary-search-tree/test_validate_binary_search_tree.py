from validate_binary_search_tree import is_valid_binary_search_tree, TreeNode
import unittest


class TestIsValidBinarySearchTree(unittest.TestCase):
    def test_returns_true_for_valid_binary_search_tree(self):
        """Takes in a valid binary search tree and returns True"""
        root = TreeNode(2)
        root.left = TreeNode(1)
        root.right = TreeNode(3)
        result = is_valid_binary_search_tree(root)
        self.assertTrue(result)

    def test_returns_false_for_invalid_binary_search_tree(self):
        """Takes in an invalid binary search tree and returns False"""
        root = TreeNode(2)
        root.left = TreeNode(5)
        root.right = TreeNode(3)
        result = is_valid_binary_search_tree(root)
        self.assertFalse(result)

    def test_returns_true_for_single_node_tree(self):
        """Takes in a single node tree and returns True"""
        root = TreeNode(1)
        result = is_valid_binary_search_tree(root)
        self.assertTrue(result)

    def test_returns_false_for_empty_tree(self):
        """Takes in an empty tree and returns False"""
        root = None
        result = is_valid_binary_search_tree(root)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()
