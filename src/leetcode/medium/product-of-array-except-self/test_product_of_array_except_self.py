from math import prod
from product_of_array_except_self import product_except_self
import unittest

class TestProductExceptSelf(unittest.TestCase):
    def test_returns_empty_list_for_empty_list(self):
        """Takes in an empty list and returns an empty one"""
        result = product_except_self([])
        self.assertEqual(result, [])

    def test_returns_correct_product_list(self):
        """Takes in a list of integers and returns the correct product list"""
        result = product_except_self([4, 7, 1, 1, 2])
        self.assertEqual(result, [14, 8, 56, 56, 28])

if __name__ == "__main__":
    unittest.main()