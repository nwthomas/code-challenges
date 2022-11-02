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

if __name__ == "__main__":
    unittest.main()