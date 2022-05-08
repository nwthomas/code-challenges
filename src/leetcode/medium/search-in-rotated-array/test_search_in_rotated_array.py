from search_in_rotated_array import search
import unittest

class TestSearchInRotatedArray(unittest.TestCase):
    def test_returns_neg_one_for_empty_array(self):
        """Takes in an empty array and returns -1 for searched number"""
        result = search([], 0)
        self.assertEqual(result, -1)

    def test_returns_neg_one_for_short_array(self):
        """Takes in a short array and returns -1 for searched number"""
        result = search([0, 1], 10)
        self.assertEqual(result, -1)

    def test_returns_index_for_short_array(self):
        """Takes in a short array and returns the index for searched number"""
        result = search([10, 0], 0)
        self.assertEqual(result, 1)

    def test_returns_index_for_rotate_array(self):
        """Takes in a rotated array and returns the index for the searched number"""
        result = search([5, 6, 7, 0, 1, 2, 3, 4], 2)
        self.assertEqual(result, 5)

    def test_returns_index_for_unrotated_array(self):
        """Takes in a non-rotated array and returns the index for the searched number"""
        result = search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 2)
        self.assertEqual(result, 2)

if __name__ == "__main__":
    unittest.main()