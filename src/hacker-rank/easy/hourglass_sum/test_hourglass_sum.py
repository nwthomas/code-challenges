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
    def test_returns_largest_sum(self):
        """Takes in a 2D array and returns the largest hourglass sum within it"""
        result = hourglassSum(self.small_2d_array)
        self.assertEqual(result, 46)

if __name__ == "__main__":
    unittest.main()