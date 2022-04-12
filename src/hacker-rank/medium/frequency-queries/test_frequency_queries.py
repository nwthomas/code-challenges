from frequency_queries import freqQuery as freq_query
import unittest

class TestFreqQuery(unittest.TestCase):
    def test_returns_correct_print_values(self):
        """Takes in a list of queries and returns print array with correct values"""
        result = freq_query([[1, 5], [1, 6], [3, 2], [1, 10], [1, 10], [1, 6], [2, 5], [3, 2]])
        self.assertEqual(result, [0, 1])

    def test_returns_empty_list(self):
        """Takes in an empty list and returns an empty list of print values"""
        result = freq_query([])
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()