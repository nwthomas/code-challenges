from array import array
from array_partition import array_pair_sum
import unittest

class TestArrayPairSum(unittest.TestCase):
    def test_returns_correct_total(self):
        """Takes in a list of unsorted numbers and returns correct total"""
        result = array_pair_sum([3, 2, 6, 4, 8, 1])
        self.assertEqual(result, 10)

    def test_handles_array_length_two(self):
        """Returns correct total for array length 2"""
        result = array_pair_sum([5, 10])
        self.assertEqual(result, 5)

    def test_handles_all_same_number(self):
        """Returns the correct total when all integers are the same"""
        result = array_pair_sum([2, 2, 2, 2, 2, 2, 2, 2])
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()