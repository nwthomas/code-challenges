from maximum_subarray import max_sub_array
import unittest

class TestMaxSubarray(unittest.TestCase):
    def test_returns_largest_sum_of_short_array_of_numbers(self):
        """Takes in a short array of numbers and returns the largest sum"""
        result = max_sub_array([5, 4, -1, 7, 8])
        self.assertEqual(result, 23)

    def test_returns_largest_sum_of_medium_array_of_numbers(self):
        """Takes in a medium array of numbers and returns the largest sum"""
        result = max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(result, 6)

if __name__ == "__main__":
    unittest.main()