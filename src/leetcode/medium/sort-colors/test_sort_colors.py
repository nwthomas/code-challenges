from sort_colors import sort_colors
import unittest

class TestSortColors(unittest.TestCase):
    def test_sorts_small_list_in_place(self):
        """Takes in a small list and sorts it in place"""
        l = [1, 0, 2, 1, 1, 2, 0, 0]
        sort_colors(l)
        self.assertEqual(l, [0, 0, 0, 1, 1, 1, 2, 2])

    def test_sorts_large_list_in_place(self):
        """Takes in a small list and sorts it in place"""
        l = [0, 1, 2, 1, 0, 0, 2, 2, 1, 1, 0, 0, 1, 0]
        sort_colors(l)
        self.assertEqual(l, [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2])

if __name__ == "__main__":
    unittest.main()