from continuous_subarray_sum import check_subarray_sum
import unittest

class TestCheckSubarraySum(unittest.TestCase):
    def test_returns_true_for_valid_subarray_sum(self):
        """Takes in list and returns True if subarray sum is possible"""
        result = check_subarray_sum([23,2,6,4,7], 6)
        self.assertTrue(result)

    def test_returns_false_for_invalid_sum(self):
        """Takes in a list and returns False if subarray sum is possible"""
        result = check_subarray_sum([23,2,6,4,7], 15)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()