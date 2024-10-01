from four_sum import four_sum
import unittest 
from collections import defaultdict
class TestFourSum(unittest.TestCase):
    def test_returns_single_four_sum(self):
        """Returns single four sum array of quadruplets from unsorted list"""
        self.assertEqual(four_sum([4, 1, 3, 2, 6, 5], 10), [[1, 2, 3, 4]])

    def test_returns_multiple_four_sum(self):
        """Returns multiple four sum array of quadruplets from unsorted list"""
        self.assertEqual(four_sum([4, 1, 3, 2, 6, 5, 2, 2], 10), [[1, 2, 2, 5], [1, 2, 3, 4], [2, 2, 2, 4]])
    
if __name__ == "__main__":
    unittest.main()