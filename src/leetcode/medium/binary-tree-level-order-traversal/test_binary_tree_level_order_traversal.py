from binary_tree_level_order_traversal import level_order, TreeNode
import unittest

class TestLevelOrder(unittest.TestCase):
    def test_traverses_tree_in_breadth_first_order(self):
        """Takes in a tree and outputs the values in breadth-first order"""
        t = TreeNode(10)
        t.right = TreeNode(15)
        t.right.left = TreeNode(14)
        t.right.right = TreeNode(20)
        t.left = TreeNode(5)
        t.left.left = TreeNode(1)
        t.left.right = TreeNode(9)

        result = level_order(t)
        self.assertEqual(result, [[10], [5, 15], [1, 9, 14, 20]])

if __name__ == "__main__":
    unittest.main()