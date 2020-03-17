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

    def test_returns_false_if_lengths_different(self):
        """
        Returns False if the lengths of the two strings input as arguments are inequal
        """
        result = are_strings_mappable("testing", "test")
        self.assertFalse(result)

    def test_returns_true_if_strings_are_mappable(self):
        """
        Returns True if one string is mappable to the other
        """
        result = are_strings_mappable("weird", "crazy")
        self.assertTrue(result)

    def test_returns_false_if_strings_are_not_mappable(self):
        """
        Returns False if one string is not mappable to the other
        """
        result = are_strings_mappable("weird", "grass")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
