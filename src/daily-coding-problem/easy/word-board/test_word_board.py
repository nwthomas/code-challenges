from word_board import is_word_present
import unittest


class TestIsWordPresent(unittest.TestCase):
    def test_finds_short_word(self):
        """
        Finds a short word in the matrix
        """
        word = "test"
        l = [["t", "e", "z", "r"], ["t", "s", "h", "l"],
             ["e", "t", "x", "a"], ["o", "p", "j", "j"]]
        result = is_word_present(l, word)
        self.assertEqual(result, True)

    def test_finds_long_word(self):
        """
        Finds a long word in the matrix
        """
        word = "testing_word"
        l = [["t", "e", "s", "t"], ["_", "g", "n", "i"],
             ["w", "t", "x", "a"], ["o", "r", "d", "j"]]
        result = is_word_present(l, word)
        self.assertEqual(result, True)

    def test_returns_false_for_no_word(self):
        """
        Returns False if the word cannot be found in the matrix
        """
        word = "testing"
        l = [["t", "d", "z", "r"], ["t", "s", "h", "l"],
             ["e", "t", "x", "a"], ["o", "p", "j", "j"]]
        result = is_word_present(l, word)
        self.assertEqual(result, False)

    def test_returns_none_for_no_list(self):
        """
        Returns None if the first argument is not a list of lists,
        or a matrix
        """
        word = "test"
        incorrect_type = {}
        result = is_word_present(incorrect_type, word)
        self.assertEqual(result, None)

    def test_returns_none_for_no_string(self):
        """
        Returns None if the second argument is not a string
        """
        incorrect_type = {}
        l = [["t", "e", "s", "t"], ["_", "g", "n", "i"],
             ["w", "t", "x", "a"], ["o", "r", "d", "j"]]
        result = is_word_present(l, incorrect_type)
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
