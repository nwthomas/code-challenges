from merge_intervals import merge
import unittest

class TestMerge(unittest.TestCase):
    def test_returns_original_list_if_no_overlap(self):
        """Takes in a list of intervals and returns the same list"""
        l = [[1, 5], [10, 15], [20, 28]]
        result = merge(l)
        self.assertEqual(result, l)

    def test_returns_empty_list(self):
        """Takes in an empty list and returns an empty list"""
        result = merge([])
        self.assertEqual(result, [])

    def test_merges_overlapping_intervals(self):
        """Takes in a list of intervals and returns with merges"""
        l = [[0, 15], [2, 8], [8, 16], [20, 23], [22, 30]]
        result = merge(l)
        self.assertEqual(result, [[0, 16], [20, 30]])

if __name__ == "__main__":
    unittest.main()