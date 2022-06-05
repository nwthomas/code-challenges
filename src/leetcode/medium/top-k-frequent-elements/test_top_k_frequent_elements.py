from top_k_frequent_elements import top_k_frequent
import unittest

class TopKFrequent(unittest.TestCase):
    def test_returns_empty_list_for_not_frequent_nums(self):
        """Takes in an empty list and returns an empty list"""
        result = top_k_frequent([], 2)
        self.assertEqual(result, [])

    def test_returns_empty_list_for_nth_frequent_nums(self):
        """Takes in a list of nums and returns the nth most frequent nums"""
        result = top_k_frequent([4, 1, 6, 2, 8, 3, 9, 4, 3, 1], 3)
        self.assertEqual(result, [1, 3, 4])

if __name__ == "__main__":
    unittest.main()