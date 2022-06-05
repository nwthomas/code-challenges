from calendar import c
from set_matrix_zeroes import set_zeroes
import unittest

class TestSetZeroes(unittest.TestCase):
    def test_does_not_modify_original_matrix_if_no_zeroes(self):
        """Takes in a matrix with no 0s and does not mutate it in place"""
        matrix = [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ]
        set_zeroes(matrix)
        self.assertEqual(matrix, [
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
        ])

    def test_sets_zeroes_for_original_matrix(self):
        """Takes in a matrix with some zeroes and mutates it in place"""
        matrix = [
            [1, 2, 3, 4, 5],
            [1, 2, 0, 4, 5],
            [1, 2, 3, 4, 0],
            [1, 2, 3, 4, 5],
            [1, 0, 3, 4, 5],
        ]
        set_zeroes(matrix)
        self.assertEqual(matrix, [
            [1, 0, 0, 4, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 0, 4, 0],
            [0, 0, 0, 0, 0],
        ])

if __name__ == "__main__":
    unittest.main()