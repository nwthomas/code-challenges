from verify_string_combos import verify_string_combos
import unittest


class TestVerifyStringCombos(unittest.TestCase):
    def test_verify_handles_non_string_first_argument(self):
        """
        Tests that the function handles a non-string passed as the first argument
        """
        result = verify_string_combos(5, "testing")
        self.assertEqual(result, None)

    def test_verify_handles_non_string_second_argument(self):
        """
        Tests that the function handles a non-string passed as the second argument
        """
        result = verify_string_combos("testing", 10)
        self.assertEqual(result, None)

    def test_returns_empty_list_if_word_longer_than_string(self):
        """
        Returns an empty list if the first argument, the word, is longer than the
        second argument, the string
        """
        result = verify_string_combos("asdfasdfasdf", "asdf")
        self.assertEqual(result, [])

    def test_returns_indices_of_found_short_combos(self):
        """
        Returns the correct indices of the start of all possible combos in a string
        of a short word
        """
        result = verify_string_combos("test", "testasdftsetest")
        self.assertEqual(result, [0, 8, 11])

    def test_returns_indices_of_found_long_combos(self):
        """
        Returns the correct indices of the start of all possible combos in a string
        of a long word
        """
        result = verify_string_combos("testing", "testingtesttingest")
        self.assertEqual(result, [0, 1, 2, 3, 4, 8, 9, 10, 11])


if __name__ == "__main__":
    unittest.main()
