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
        ]
        result = get_alien_language_order(dictionary)
        self.assertEqual(result, "abcdefghij")

if __name__ == "__main__":
    unittest.main()