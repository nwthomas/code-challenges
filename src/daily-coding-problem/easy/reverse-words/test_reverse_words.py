from reverse_words import reverse_words
import unittest


class TestReverseWords(unittest.TestCase):
    def test_returns_none_if_not_string_argument(self):
        """
        Returns None if the argument passed in is not a string
        """
        result = reverse_words([1, 2, 3, 4])
        self.assertIsNone(result)

    def test_reverses_short_string_of_words(self):
        """
        Reverse a short string of space-delimited words
        """
        result = reverse_words("nathan thomas wrote this sentence")
        self.assertEqual(result, "sentence this wrote thomas nathan")

    def test_reverses_long_string_of_words(self):
        """
        Reverses a long string of space-delimited words
        """
        result = reverse_words(
            "this is a long sentence that is being used to test the functionality of the function")
        self.assertEqual(
            result, "function the of functionality the test to used being is that sentence long a is this")


if __name__ == "__main__":
    unittest.main()
