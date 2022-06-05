from shifted_array_search import shifted_arr_search
import unittest

class TestShiftedArrSearch(unittest.TestCase):
    def test_returns_neg_one_for_empty_list(self):
        """Takes in an empty list and returns -1"""
        result = shifted_arr_search([], 1)
        self.assertEqual(result, -1)

    def test_finds_correct_position(self):
        """Takes in a list and a number and finds its position"""
        result = shifted_arr_search([4, 5, 7, 1, 2, 3], 5)
        self.assertEqual(result, 1)

    def test_returns_neg_one_if_not_found(self):
        """Takes in a list and a number and returns -1 if not found"""
        result = shifted_arr_search([5, 6, 7, 8, 1, 2, 3], 10)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()