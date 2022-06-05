from maximum_depth_of_binary_tree import max_depth, TreeNode
import unittest

class TestMaxDepth(unittest.TestCase):
    def test_returns_zero_if_no_tree(self):
        """Returns 0 if there is no tree to traverse"""
        result = max_depth(root=None)
        self.assertEqual(result, 0)

    def test_returns_max_depth_of_tree(self):
        t = TreeNode(10)
        t.right = TreeNode(20)
        t.right.left = TreeNode(19)
        t.right.left.left = TreeNode(18)
        t.left = TreeNode(5)
        t.left.right = TreeNode(8)

        result = max_depth(t)
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()