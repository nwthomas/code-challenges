from non_overlapping_intervals import erase_overlapping_intervals
import unittest

class TestEraseOverlappingIntervals(unittest.TestCase):
    def test_does_not_remove_intervals_if_not_needed(self):
        """Takes in some intervals and does not remove any"""
        result = erase_overlapping_intervals([[1, 2], [5, 6]])
        self.assertEqual(result, 0)

    def test_removes_overlapping_intervals(self):
        """Takes in some intervals and removes overlapping ones"""
        result = erase_overlapping_intervals([[1, 2], [4, 5], [4, 7]])
        self.assertEqual(result, 1)

    def test_can_handle_multiple_overlaps(self):
        """Takes in some intervals with multiple overlaps and returns correct removed count"""
        result = erase_overlapping_intervals([[1, 100], [3, 4], [7, 100]])
        self.assertEqual(result, 1)

if __name__ == "__main__":
    unittest.main()