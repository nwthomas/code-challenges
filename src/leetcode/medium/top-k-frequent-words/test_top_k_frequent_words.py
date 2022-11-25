from top_k_frequent_words import topKFrequent
import unittest

class TestTopKFrequent(unittest.TestCase):
    def test_returns_correct_words_in_order_short_list(self):
        """Takes in a short list of words and returns the correct response in order"""
        w = ["i", "love", "you", "i", "i", "you"]
        result = topKFrequent(w, 2)
        self.assertEqual(result, ["i", "you"])

    def test_returns_correct_words_for_long_list(self):
        """Takes in a long list of words and returns the correct response in order"""
        w = ["if", "you", "read", "this", "dm", "me", "if", "you", "want", "this", "if", "this"]
        result = topKFrequent(w, 5)
        self.assertEqual(result, ["if", "this", "you", "dm", "me"])

if __name__ == "__main__":
    unittest.main()