from sherlock_and_anagrams import sherlock_and_anagrams
import unittest

class TestSherlockAndAnagrams(unittest.TestCase):
    def test_returns_count_when_is_anagram(self):
        """Returns the correct count when an anagram is possible"""
        result = sherlock_and_anagrams("abba");
        self.assertEqual(result, 4)

    def test_returns_count_zero_when_not_anagram(self):
        """Returns 0 as the correct count when an anagram is not possible"""
        result = sherlock_and_anagrams("abcd")
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()