from greatest_common_denominator import find_greatest_common_denominator
import unittest


class TestFindGreatestCommonDenominator(unittest.TestCase):
    def test_returns_common_denominator_small_list(self):
        """
        Takes in a small number list and returns the lowest common denominator
        """
        result = find_greatest_common_denominator([45, 25, 15])
        self.assertEqual(result, 5)

    def test_returns_common_denominator_large_list(self):
        """
        Takes in a large number list and returns the lowest common denominator
        """
        result = find_greatest_common_denominator([15, 19, 4, 16, 19, 10, 60])
        self.assertEqual(result, 5)


if __name__ == "__main__":
    unittest.main()
