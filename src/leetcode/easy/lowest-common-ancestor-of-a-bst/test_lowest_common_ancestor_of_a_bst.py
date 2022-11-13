from lowest_common_ancestor_of_a_bst import lowest_common_ancestor, TreeNode
import unittest

class TestLowestCommonAncestor(unittest.TestCase):
    def test_returns_lowest_common_ancestor(self):
        """Takes in a tree with two values and finds their lowest common ancestor"""
        root = TreeNode(8)
        root.right = TreeNode(10)
        root.left = TreeNode(5)
        root.right.left = TreeNode(9)
        root.right.right = TreeNode(15)
        root.left.left = TreeNode(7)
        root.left.right = TreeNode(1)

        result = lowest_common_ancestor(root, root.right.right, root.left.right)
        self.assertEqual(result, root)

if __name__ == "__main__":
    unittest.main()