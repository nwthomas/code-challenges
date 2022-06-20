from kth_smallest_element_in_bst import kth_smallest, TreeNode
import unittest

class TestKthSmallest(unittest.TestCase):
    def test_returns_kth_smallest_of_small_tree(self):
        """Takes in a small tree and returns the kth smallest element"""
        root = TreeNode(5, TreeNode(3, TreeNode(1), TreeNode(4)), TreeNode(7, TreeNode(6)))
        result = kth_smallest(root, 2)
        self.assertEqual(result, 3)

    def test_returns_kth_smallest_of_larger_tree(self):
        root = TreeNode(5, TreeNode(3, TreeNode(1, TreeNode(0), TreeNode(2)), TreeNode(4, None, TreeNode(4))), TreeNode(7, TreeNode(6), TreeNode(10, None, TreeNode(15, None, TreeNode(20)))))
        result = kth_smallest(root, 8)
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()