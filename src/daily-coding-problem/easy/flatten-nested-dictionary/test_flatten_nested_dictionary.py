from flatten_nested_dictionary import flatten_nested_dictionary
import unittest


class TestFlattenNestedDictionary(unittest.TestCase):
    def test_returns_empty_dict(self):
        """
        Returns an empty dictionary if the first argument is an empty dictionary
        """
        result = flatten_nested_dictionary({})
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
