from median_of_two_sorted_arrays import find_median_sorted_arrays
import unittest

class TestFindMedianSortedArrays(unittest.TestCase):
    def test_returns_median_short_lists(self):
        """Takes in two short lists and returns the median"""
        result = find_median_sorted_arrays([1, 2], [3, 4])
        self.assertEqual(result, 2.5)

    def test_returns_median_long_lists(self):
        """Takes in two longer lists and returns the midpoint"""
        result = find_median_sorted_arrays([1, 4, 7, 10, 15, 41], [3, 19, 40, 300, 301])
        self.assertEqual(result, 15)
    
    def test_handles_lists_length_one(self):
        """Takes in two lists of length 1 and returns the median of them"""
        result = find_median_sorted_arrays([1], [2])
        self.assertEqual(result, 1.5)

if __name__ == "__main__":
    unittest.main()