from lowest_common_ancestor import lowestCommonAncestor, TreeNode
import unittest

class TestLowestCommonAncestor(unittest.TestCase):
    def test_returns_lowest_common_ancestor(self):
        """Takes in a tree and two nodes and returns the lowest common ancestor"""
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(7)
        root.right.right = TreeNode(9)
        root.left.right.left = TreeNode(3)
        root.left.right.right = TreeNode(5)

        p = root.left
        q = root.right

        result = lowestCommonAncestor(root, p, q)
        self.assertEqual(result, root)

    def test_returns_lowest_common_ancestor_when_one_node_is_ancestor(self):
        """Takes in a tree and two nodes where one is the ancestor and returns the ancestor"""
        root = TreeNode(6)
        root.left = TreeNode(2)
        root.right = TreeNode(8)
        root.left.left = TreeNode(0)

        p = root.left
        q = root.left.left

        result = lowestCommonAncestor(root, p, q)
        self.assertEqual(result, root.left)

if __name__ == "__main__":
    unittest.main()