from reverse_words_in_place import reverse_words_in_place, reverse_subsection_list
import unittest


class TestReverseSubstringString(unittest.TestCase):
    def test_reverses_partial_list_from_indices_given(self):
        """Reverses only the subsection of a list chars based on the provided indices"""
        l = ["t", "e", "s", "t"]
        reverse_subsection_list(l, 0, 1)
        self.assertEqual(l, ["e", "t", "s", "t"])

    def test_reverses_full_list_from_indices_given(self):
        """Reverses the entire list of chars based on the provided indices"""
        l = ["t", "e", "s", "t"]
        reverse_subsection_list(l, 0, 3)
        self.assertEqual(l, ["t", "s", "e", "t"])


class TestReverseWordsInPlace(unittest.TestCase):
    def test_leaves_single_char_in_list_alone(self):
        """Does not mutate a single char inside a list"""
        l = ["Q"]
        reverse_words_in_place(l)
        self.assertEqual(l, ["Q"])

    def test_reverses_full_list_of_chars(self):
        """Reverses an entire list of chars in place inside a list"""
        l = ["t", "e", "s", "t", " ", "t", "h", "i", "s"]
        reverse_words_in_place(l)
        self.assertEqual(l, ["t", "h", "i", "s", " ", "t", "e", "s", "t"])


if __name__ == "__main__":
    unittest.main()
