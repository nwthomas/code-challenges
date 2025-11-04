from length_of_longest_substring_without_repeating_character import lengthOfLongestSubstring
import unittest

class TestLengthOfLongestSubstringWithoutRepeatingCharacter(unittest.TestCase):
    def test_length_of_longest_substring_without_repeating_character(self):
        """Takes in a string and returns the length of the longest substring without repeating characters"""
        result = lengthOfLongestSubstring("abcabcbb")
        self.assertEqual(result, 3)

        result = lengthOfLongestSubstring("bbbbb")
        self.assertEqual(result, 1)

        result = lengthOfLongestSubstring("pwwkew")
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()