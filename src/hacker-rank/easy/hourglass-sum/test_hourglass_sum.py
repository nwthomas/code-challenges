from hourglass_sum import hourglassSum
import unittest

class TestHourglassSum(unittest.TestCase):
    small_2d_array = [
        [1, 2, 3, 4],
        [0, 9, 8, 7],
        [3, 5, 1, 2],
        [10, 5, 9, 2],
        [8, 9, 3, 4]
    ]

    large_2d_array = [
        [1, 2, 3, 4, 3, 8, 2, 5],
        [0, 9, 8, 7, 8, 19, 3, 0],
        [3, 5, 1, 2, 10, 3, 5, 2],
        [10, 5, 9, 2, 5, 9, 23, 1],
        [8, 9, 3, 4, 0, 0, 4, 1]
    ]


    def test_returns_largest_sum_small_array(self):
        """Takes in a small 2D array and returns the largest hourglass sum within it"""
        result = hourglassSum(self.small_2d_array)
        self.assertEqual(result, 46)

    def test_returns_largest_sum_large_array(self):
        """Takes in a large 2D array and reutnrs the largest hourglass sum within it"""
        result = hourglassSum(self.large_2d_array)
        self.assertEqual(result, 70)

    def test_returns_zero_if_no_values(self):
        """Takes in an empty array and returns 0 as the default value"""
        result = hourglassSum([])
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()