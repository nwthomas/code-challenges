from first_recurring_char import find_first_recurring_char
import unittest


class TestFindFirstRecurringChar(unittest.TestCase):
    def test_returns_none_if_no_recurring_chars(self):
        """
        Takes in a string and returns None if no recurring characters are found
        """
        result = find_first_recurring_char("abcdefg")
        self.assertIsNone(result)

    def test_returns_first_recurring_char_short_string(self):
        """
        Takes in a short string and returns the first recurring character
        """
        result = find_first_recurring_char("abcdagtf")
        self.assertEqual(result, "a")

    def test_returns_first_recurring_char_long_string(self):
        """
        Takes in a long string and returns the first recurring character among many
        """
        result = find_first_recurring_char("abcdefghijkajcdbeadbe")
        self.assertEqual(result, "a")


if __name__ == "__main__":
    unittest.main()
