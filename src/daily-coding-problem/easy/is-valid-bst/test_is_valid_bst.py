from is_valid_bst import BinaryTree, is_valid_binary_search_tree
import unittest

values = [7, 3, 8, 9, 3, 6, 10]

class TestIsValidBST(unittest.TestCase):
    def test_return_true(self):
        bst = self._create_valid_bst()
        result = is_valid_binary_search_tree(bst)
        self.assertTrue(result)

    def test_returns_false(self):
        bst = self._create_invalid_bst()
        result = is_valid_binary_search_tree(bst)
        self.assertFalse(result)

    def _create_valid_bst(self):
        bst = BinaryTree(values[0])

        for index, value in enumerate(values):
            if index > 0:
                bst.add_value_to_tree(value)

        return bst

    def _create_invalid_bst(self):
        bst = self._create_valid_bst()
        bst.root.left.value = 1000000

        return bst



if __name__ =="__main__":
    unittest.main()