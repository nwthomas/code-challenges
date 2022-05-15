from gettext import find
from first_missing_positive import find_first_missing_positive
import unittest

class TestFindFirstMissingPositive(unittest.TestCase):
    def test_returns_first_missing_positive_if_one(self):
        """Takes in a list of numbers with 1 missing and returns it"""
        result = find_first_missing_positive([4, -1, 5, 10])
        self.assertEqual(result, 1)

    def test_returns_first_missing_positive(self):
        """Takes in a list of numbers and returns the first missing positive"""
        result = find_first_missing_positive([3,4,-1,1])
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()