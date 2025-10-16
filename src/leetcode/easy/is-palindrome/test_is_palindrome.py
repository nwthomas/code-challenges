import unittest

from is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("race a car"))
        self.assertTrue(is_palindrome(" "))
        self.assertTrue(is_palindrome(""))
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("123321"))
        self.assertTrue(is_palindrome("1234321"))
        self.assertTrue(is_palindrome("1234567890987654321"))

if __name__ == "__main__":
    unittest.main()