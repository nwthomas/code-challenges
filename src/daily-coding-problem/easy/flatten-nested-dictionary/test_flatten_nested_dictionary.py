from flatten_nested_dictionary import flatten_nested_dictionary
import unittest


class TestFlattenNestedDictionary(unittest.TestCase):
    def test_returns_empty_dict(self):
        """
        Returns an empty dictionary if the first argument is an empty dictionary
        """
        result = flatten_nested_dictionary({})
        self.assertEqual(result, {})

    def test_throws_new_error(self):
        """
        Throws a new TypeError if the first argument is not a dictionary
        """
        def result(): return flatten_nested_dictionary("test")
        self.assertRaises(TypeError, result)

    def test_flattens_small_dictionary(self):
        """
        Flattens a small dictionary
        """
        dictionary = {"a": 1, "b": {"c": 2, "d": {"e": 3}}}
        result = flatten_nested_dictionary(dictionary)
        self.assertEqual(result, {"a": 1, "b.c": 2, "b.d.e": 3})

    def test_flattens_large_dictionary(self):
        """
        Flattens a large dictionary
        """
        dictionary = {"a": 1, "b": {"c": 2, "d": {
            "e": 3, "f": 4, "g": {"h": 5}, "i": 6}}, "j": {"k": 7}}
        result = flatten_nested_dictionary(dictionary)
        self.assertEqual(result, {
                         'a': 1, 'b.c': 2, 'b.d.e': 3, 'b.d.f': 4, 'b.d.g.h': 5, 'b.d.i': 6, 'j.k': 7})


if __name__ == "__main__":
    unittest.main()
