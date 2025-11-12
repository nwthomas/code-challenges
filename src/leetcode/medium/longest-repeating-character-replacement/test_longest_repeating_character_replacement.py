from longest_repeating_character_replacement import characterReplacement
import unittest

class TestCharacterReplacement(unittest.TestCase):
    def test_replacement_short_string(self):
        """Takes in a short string with small number of replacements and returns the longest substring with the same letter"""
        result = characterReplacement("ABAB", 2)
        self.assertEqual(result, 4)

    def test_replacement_long_string(self):
        """Takes in a long string with large number of replacements and returns the longest substring with the same letter"""
        result = characterReplacement("AABABBACD", 1)
        self.assertEqual(result, 4)

    def test_replacement_string_with_no_replacements(self):
        """Takes in a string with no replacements and returns the length of the string"""
        result = characterReplacement("ABC", 0)
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()