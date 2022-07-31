from longest_palindrome_subsequence import get_longest_palindrome_subsequence
import unittest

class TestGetLongestPalindromeSubsequence(unittest.TestCase):
    def test_returns_longest_common_palindrome_subsequence(self):
        """Takes in a string and returns the longest common palindrome subsequence"""
        result = get_longest_palindrome_subsequence("anagram")
        self.assertEqual(result, 3)

    def test_returns_one_if_no_common_palindrome_subsequence(self):
        """Takes in a string and returns 1 for 1 char if no common palindrome subsequence"""
        result = get_longest_palindrome_subsequence("abcxyz")
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()