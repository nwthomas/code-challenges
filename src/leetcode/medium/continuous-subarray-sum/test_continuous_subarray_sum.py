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

    def test_raises_typeerror_if_not_list(self):
        """Raises a new TypeError if the first argument is not of type list"""
        def result():
            return check_subarray_sum({}, 10)

        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_not_int(self):
        """Raises a new TypeError if the second argument is not of type int"""
        def result():
            return check_subarray_sum([1, 2, 3], True)

        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()