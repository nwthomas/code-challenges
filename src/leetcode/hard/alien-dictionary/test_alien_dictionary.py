from alien_dictionary import get_alien_language_order
import unittest

class TestGetAlienLanguageOrder(unittest.TestCase):
    def test_finds_order_in_short_dictionary(self):
        """Takes in a short alien dictionary and returns the right word order"""
        dictionary = [
            "wrt",
            "wrf",
            "er",
            "ett",
            "rftt"
        ]
        result = get_alien_language_order(dictionary)
        self.assertEqual(result, "wertf")

    def test_finds_order_in_long_dictionary(self):
        """Finds the correct word order in a longer dictionary"""
        dictionary = [
            "ab",
            "bc",
            "cd",
            "de",
            "ef",
            "fg",
            "gh",
            "hi",
            "ij",
            "jk",
            "kl",
            "lm",
        ]
        result = get_alien_language_order(dictionary)
        self.assertEqual(result, "abcdefghijklm")

    def test_returns_empty_string_for_invalid_dictionary(self):
        """Returns an empty string for an invalid dictionary"""
        dictionary = [
            "abc",
            "a"
        ]
        result = get_alien_language_order(dictionary)
        self.assertEqual(result, "")

if __name__ == "__main__":
    unittest.main()