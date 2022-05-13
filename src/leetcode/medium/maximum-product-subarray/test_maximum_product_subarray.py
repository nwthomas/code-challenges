from maximum_product_subarray import max_product
import unittest

class TestMaxProduct(unittest.TestCase):
    def test_returns_only_value_if_array_length_one(self):
        """Takes in an array of length 1 and returns the value"""
        result = max_product([10101])
        self.assertEqual(result, 10101)

    def test_returns_largest_product_within_array(self):
        """Takes in an array and returns the largest contiguous product"""
        result = max_product([2,3,-2,4,10,-5,3,2,1])
        self.assertEqual(result, 14400)

if __name__ == "__main__":
    unittest.main()