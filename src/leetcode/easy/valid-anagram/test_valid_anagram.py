from valid_anagram import is_anagram
import unittest

class TestIsAnagram(unittest.TestCase):
    def test_returns_true_if_anagram(self):
        """Returns True if words are anagrams"""
        result = is_anagram("anagram", "nagaram")
        self.assertTrue(result)

    def test_returns_false_if_not_anagram(self):
        """Returns False if words are not anagrams"""
        result = is_anagram("testing", "graham")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()