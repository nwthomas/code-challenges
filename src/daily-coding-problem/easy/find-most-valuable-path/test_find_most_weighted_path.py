from find_most_weighted_path import find_most_weighted_path_down
import unittest

large_triangle = [[6], [3, 6, 8], [1, 2, 1, 5, 1], [9, 10, 15, 0, 0, 0, 1]]
small_triangle = [[3], [1, 7], [9, 4, 3]]

class TestFindMostWeightedPath(unittest.TestCase):
    def test_returns_correct_num_for_small_triangle(self):
        result = find_most_weighted_path_down(small_triangle)
        self.assertEqual(result, 14)

    def test_returns_correct_num_for_large_triangle(self):
        result = find_most_weighted_path_down(large_triangle)
        self.assertEqual(result, 29)


if __name__ == "__main__":
    unittest.main()