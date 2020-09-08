from permutation_palindrome import is_permutation_palindrome
import unittest


class TestIsPermutationPalindrome(unittest.TestCase):
    def test_returns_true_if_possible_palindrome(self):
        """Returns true if a palindrome is possible with a given permutation of a string"""
        result = is_permutation_palindrome("hdhdiuigygyoioi")
        self.assertTrue(result)

    def test_returns_false_if_not_possible_palindrome(self):
        """Returns false if a palindrome is not possible with a given permutation of a string"""
        result = is_permutation_palindrome("ahsidfha")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
