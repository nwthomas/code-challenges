import unittest

from two_integer_sum_ii import twoSum


# Class that tests two integer sum ii which uses sorted lists
class TestTwoIntegerSumII(unittest.TestCase):
    def test_returns_indices(self):
        """Takes in a list of numbers and returns the targeted indices if sum is possible"""
        result = twoSum([1, 2, 3, 4, 6, 10], 3)
        self.assertEqual(result, [1, 2])

    def test_returns_empty_list(self):
        """Returns empty list if a sum is not possible"""
        result = twoSum([1, 2, 3, 4, 6, 10], 100)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()