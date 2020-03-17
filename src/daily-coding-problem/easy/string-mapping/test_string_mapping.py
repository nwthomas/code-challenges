from string_mapping import are_strings_mappable
import unittest


class TestAreStringsMappable(unittest.TestCase):
    def test_throws_error_if_not_strings(self):
        """
        Throws a TypeError if either of the arguments are a string
        """
        def result_one(): return are_strings_mappable({}, "test")
        def result_two(): return are_strings_mappable("test", {})
        self.assertRaises(TypeError, result_one)
        self.assertRaises(TypeError, result_two)


if __name__ == "__main__":
    unittest.main()
