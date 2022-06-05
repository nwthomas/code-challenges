from invert_binary_tree import invert_tree, TreeNode
import unittest

class TestInvertTree(unittest.TestCase):
    def test_inverts_binary_tree(self):
        """Takes in a tree and inverts it"""
        t = TreeNode(10)
        t.left = TreeNode(4)
        t.right = TreeNode(15)

        result = invert_tree(t)
        self.assertEqual(result.val, 10)
        self.assertEqual(result.right.val, 4)
        self.assertEqual(result.left.val, 15)

if __name__ == "__main__":
    unittest.main() 