from valid_sentence_checker import is_valid_sentence
import unittest


class TestIsValidSentence(unittest.TestCase):
    def test_returns_true_if_valid_sentence(self):
        """Takes in a valid sentence and returns True"""
        result = is_valid_sentence("This is a good sentence?")
        self.assertTrue(result)

    def test_returns_true_for_multiple_good_sentences(self):
        """Takes in multiple valid sentences and returns true"""
        result = is_valid_sentence("This is sentence one. This is sentence two?")
        self.assertTrue(result)

    def test_returns_false_if_not_starting_capital(self):
        """Takes in an invalid sentence with no starting capital letter and returns False"""
        result = is_valid_sentence("this is a bad sentence with no capital letter.")
        self.assertFalse(result)
    
    def test_returns_false_if_extra_spaces(self):
        """Takes in an invalid sentence with extra spaces and returns False"""
        result = is_valid_sentence("Sentence one.  Sentence two.")
        self.assertFalse(result)
    
    def test_returns_false_if_invalid_terminal_character(self):
        """Takes in invalid sentence with invalid terminal character and returns False"""
        result = is_valid_sentence("Test sentence;")
        self.assertFalse(result)
    
    def test_returns_false_if_multiple_spaces_at_end(self):
        """Takes in an invalid sentence with multiple spaces at the end and returns false"""
        result = is_valid_sentence("Test sentence.       ")
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()