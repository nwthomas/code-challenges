from wildcard_brackets import is_balanced_parentheses_string
import unittest

class TestIsBalancedParenthesesString(unittest.TestCase):
    def test_raises_typeerror_if_not_string(self):
        def result(): return is_balanced_parentheses_string({ "test": "test" })
        self.assertRaises(TypeError, result)

    def test_returns_false_for_empty_string(self):
        result = is_balanced_parentheses_string("")
        self.assertFalse(result)

    def test_returns_true_for_balanced_string(self):
        result = is_balanced_parentheses_string("()")
        self.assertTrue(result)

    def test_returns_false_for_imbalanced_string(self):
        result = is_balanced_parentheses_string("()(")
        self.assertFalse(result)
    
    def test_handles_wildcard_character(self):
        result = is_balanced_parentheses_string("(*((()*)")
        self.assertTrue(result)
    
    def test_handles_whole_string_of_wildcard_characters(self):
        result = is_balanced_parentheses_string("********")
        self.assertTrue(result)
    
    def test_returns_false_for_imbalanced_string_with_wildcard(self):
        result = is_balanced_parentheses_string("***(*")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()