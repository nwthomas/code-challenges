from valid_parentheses import get_is_valid_parentheses
import unittest

class TestGetIsValidParentheses(unittest.TestCase):
    def test_is_not_valid_parentheses_sets(self):
        """Takes in a string of parentheses that aren't valid and returns False"""
        result = get_is_valid_parentheses("{)(}")
        self.assertFalse(result)

    def test_is_valid_parentheses_sets(self):
        """Takes in a string of parentheses that are valid and returns True"""
        result = get_is_valid_parentheses("()[]{}")
        self.assertTrue(result)

    def test_returns_true_for_empty_string(self):
        """Takes in an empty string and returns True"""
        result = get_is_valid_parentheses("")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()