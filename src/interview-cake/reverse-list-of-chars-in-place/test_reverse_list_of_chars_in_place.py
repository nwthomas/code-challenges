from reverse_list_of_chars_in_place import reverse_list_of_chars_in_place
import unittest


class TestReverseListOfCharsInPlace(unittest.TestCase):
    def test_raises_typeerror_if_not_of_type_list(self):
        """Raises a new TypeError if the argument given is not of type list"""
        def result(): return reverse_list_of_chars_in_place("test")
        self.assertRaises(TypeError, result)

    def test_reverse_list_of_chars_in_place(self):
        """Returns a list of characters reversed in place"""
        list_of_chars = ["t", "e", "s", "t"]
        reverse_list_of_chars_in_place(list_of_chars)
        self.assertEqual(list_of_chars, ["t", "s", "e", "t"])


if __name__ == "__main__":
    unittest.main()
