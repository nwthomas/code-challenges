from coin_collector import find_most_coins_path
import unittest


class TestFindMostCoinPath(unittest.TestCase):
    def test_returns_none_if_no_matrix(self):
        """
        Returns None if the matrix is not a list
        """
        result = find_most_coins_path("test")
        self.assertIsNone(result)

    def test_returns_none_if_empty_matrix(self):
        """
        Returns None if the matrix is lesser-than-or-equal-to 0
        """
        result = find_most_coins_path(0)
        self.assertIsNone(result)

    def test_returns_correct_total_coins_for_small_matrix(self):
        """
        Takes in a small 2D matrix of numbers and returns the correct total
        """
        matrix = [[0, 1, 2], [7, 5, 0], [0, 4, 3]]
        result = find_most_coins_path(matrix)
        self.assertEqual(result, 19)

    def test_returns_correct_total_coins_for_large_matrix(self):
        """
        Takes in a large 2D matrix of numbers and returns the correct total
        """
        matrix = [[3, 6, 7, 8, 9, 0], [0, 0, 0, 0, 0, 0], [1, 1, 1, 4, 5, 6], [
            0, 0, 4, 6, 0, 0], [8, 4, 6, 3, 2, 1], [0, 0, 0, 0, 0, 0]]
        result = find_most_coins_path(matrix)
        self.assertEqual(result, 45)


if __name__ == "__main__":
    unittest.main()
