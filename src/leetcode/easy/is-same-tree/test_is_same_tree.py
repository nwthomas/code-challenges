from is_same_tree import is_same_tree, TreeNode
import unittest

class TestIsSameTree(unittest.TestCase):
    def test_returns_false_if_different_tree(self):
        """Takes in two trees and returns False when different"""
        t1 = TreeNode(1)
        t1.left = TreeNode(0)
        t1.right = TreeNode(10)

        t2 = TreeNode(4)

        result = is_same_tree(t1, t2)
        self.assertFalse(result)

    def test_returns_true_if_same_tree(self):
        """Takes in two trees and returns True when same"""
        t1 = TreeNode(1)
        t1.left = TreeNode(0)
        t1.right = TreeNode(10)

        result = is_same_tree(t1, t1)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()