from three_sum import three_sum
import unittest

class TestThreeSum(unittest.TestCase):
    short_list = [-1, 0, 3, 5, -2, -2, 0, 4, 3, 5]
    long_list = [-1, 0, 3, 5, -2, -2, 0, 4, 3, 5, 9, -8, -3, -8, 8, 9, 10, -5]

    def test_returns_empty_list(self):
        """Takes in a list of less than length 3 and returns an empty list"""
        result = three_sum([1, 2])
        self.assertEqual(result, [])

    def test_returns_correct_sets_from_short_list(self):
        """Takes in a short list of numbers and returns the correct sets adding up to 0"""
        result = three_sum(self.short_list)
        self.assertEqual(result, [(-2, -1, 3), (-2, -2, 4)])

    def test_returns_correct_sets_from_long_list(self):
        """Takes in a long list of numbers and returns the correct sets adding up to 0"""
        result = three_sum(self.long_list)
        self.assertEqual(result, [
            (-3, -1, 4),
            (-5, -3, 8),
            (-8, 3, 5),
            (-8, 0, 8),
            (-2, -2, 4),
            (-3, 0, 3),
            (-8, -2, 10),
            (-2, -1, 3),
            (-3, -2, 5),
            (-5, 0, 5),
            (-8, -1, 9)
        ])

if __name__ == "__main__":
    unittest.main()