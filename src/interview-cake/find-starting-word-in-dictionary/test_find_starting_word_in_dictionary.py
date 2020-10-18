from find_starting_word_in_dictionary import find_rotation_point
import unittest

long_words_list = [
    'nathan',
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]

short_words_list = [
    'banoffee',
    'undulate',
    'xenoepist',
    'appreciate',
    'asymptote',
    'babka',
]


class TestFindRotationPoint(unittest.TestCase):
    def test_raises_typeerror_if_not_list(self):
        """Raises a new TypeError if the inputted argument is not of type list"""
        def result(): return find_rotation_point("test")
        self.assertRaises(TypeError, result)

    def test_returns_single_phrase_if_len_one(self):
        """Returns the zero index in a list if the list is of length one"""
        result = find_rotation_point(["nathan"])
        self.assertEqual(result, 0)

    def test_returns_none_if_empty_list(self):
        """Returns None if the list argument is empty"""
        result = find_rotation_point([])
        self.assertIsNone(result)

    def test_finds_rotation_point_in_short_list(self):
        """Finds the rotation point index in a short list of strings"""
        result = find_rotation_point(short_words_list)
        self.assertEqual(result, 3)

    def test_finds_rotation_point_in_long_list(self):
        """Finds the rotation point string in a long list of strings"""
        result = find_rotation_point(long_words_list)
        self.assertEqual(result, 6)


if __name__ == "__main__":
    unittest.main()
