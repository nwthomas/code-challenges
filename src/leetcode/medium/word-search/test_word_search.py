from typing import Type
from word_search import does_word_exist
import unittest

class TestExist(unittest.TestCase):
    def test_finds_word_horizontally(self):
        """Finds a word in a horizontal row"""
        result = does_word_exist([["s", "e", "e"], ["f", "r", "c"], ["r", "q", "a"]], "see")
        self.assertTrue(result)

    def test_finds_word_vertically(self):
        """Finds a word in a vertical column"""
        result = does_word_exist([["r", "t", "b"], ["e", "i", "o"], ["g", "p", "l"]], "tip")
        self.assertTrue(result)

    def test_finds_word_curving_around_rows_and_columns(self):
        """Finds a word that meanders around rows and columns"""
        result = does_word_exist([["r", "e", "a"], ["t", "l", "l"], ["q", "y", "m"]], "really")
        self.assertTrue(result)

    def test_returns_false_if_no_word(self):
        """Returns False if no word is found"""
        result = does_word_exist([["s", "e", "e"], ["f", "r", "c"], ["r", "q", "a"]], "quite")
        self.assertFalse(result)

    def test_raises_typeerror_if_not_list(self):
        """Raises TypeError if first argument base data structure is not list"""
        def result():
            return does_word_exist("test", "test")

        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_row_not_list(self):
        """Raises TypeError if row within list is not of type list"""
        def result():
            return does_word_exist([["y", "t", "e"], "yes", ["t", "l", "b"]], "test")
        
        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_cells_arent_type_string(self):
        """Raises TypeError if cells within board aren't of type string"""
        def result():
            return does_word_exist([["r", "t", "b"], ["e", "i", 45615423], ["g", "p", "l"]], "test")

        self.assertRaises(TypeError, result)

    def test_raises_if_second_arg_not_string(self):
        """Raises TypeError if second argument of word is not of type string"""
        def result():
            return does_word_exist([["r", "t", "b"], ["e", "i", "o"], ["g", "p", "l"]], [[[[]]]])
        
        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()