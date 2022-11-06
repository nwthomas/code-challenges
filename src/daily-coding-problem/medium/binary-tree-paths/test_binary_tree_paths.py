from binary_tree_paths import get_binary_tree_paths, TreeNode
import unittest

class TestGetBinaryTreePaths(unittest.TestCase):
    def test_gets_paths_for_small_tree(self):
        """Gets all the paths to leaves for a small binary tree"""
        root = TreeNode(10)
        root.left = TreeNode(3)
        root.right = TreeNode(15)

        result = get_binary_tree_paths(root)
        self.assertEqual(result, [[10, 15], [10, 3]])

    def test_gets_paths_for_larger_tree(self):
        """Gets all the paths to leaves for a larger binary tree"""
        root = TreeNode(10)
        root.left = TreeNode(8)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(9)
        root.right = TreeNode(20)
        root.right.right = TreeNode(25)
        root.right.right.right = TreeNode(30)
        root.right.right.left = TreeNode(24)

        result = get_binary_tree_paths(root)
        self.assertEqual(result, [[10, 20, 25, 30], [10, 20, 25, 24], [10, 8, 9], [10, 8, 5]])

if __name__ == "__main__":
    unittest.main()