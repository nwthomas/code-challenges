from maximal_square import maximal_square
import unittest

class TestMaximalSquare(unittest.TestCase):
    def test_returns_zero_if_no_ones(self):
        """Takes in a matrix of 0s and returns 0"""
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        result = maximal_square(matrix)
        self.assertEqual(result, 0)

    def test_returns_one_for_one_cell(self):
        """Takes in a matrix with only one 1 and returns 1"""
        matrix = [
            [0, 0, 1],
            [0, 0, 0],
            [0, 0, 0],
        ]

        result = maximal_square(matrix)
        self.assertEqual(result, 1)

    def test_can_dynamically_calculate_larger_square_areas(self):
        """Takes in a large matrix with a large square area and returns result"""
        matrix = [
            [1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 0, 0, 0],
        ]

        result = maximal_square(matrix)
        self.assertEqual(result, 9)

if __name__ == "__main__":
    unittest.main()