from longest_common_subsequence import get_longest_common_subsequence
import unittest

class TestGetLongestCommonSubsequence(unittest.TestCase):
    def test_returns_correct_value_for_short_strings(self):
        """Takes in two short strings and returns the longest common subsequence"""
        result = get_longest_common_subsequence("testing", "testi")
        self.assertEqual(result, 5)

    def test_returns_correct_value_for_long_strings(self):
        """Takes in two long strings and returns the longest common subsequence"""
        result = get_longest_common_subsequence("this is a test of commononality", "test of common")
        self.assertEqual(result, 14)

    def test_returns_zero(self):
        """Takes in empty strings and returns 0"""
        result = get_longest_common_subsequence("", "")
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()