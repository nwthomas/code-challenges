from insert_interval import insert
import unittest

class TestInsert(unittest.TestCase):
    def test_returns_new_interval_if_empty_list(self):
        """Takes in no intervals + new interval and returns new interval"""
        result = insert([], [5, 6])
        self.assertEqual(result, [[5, 6]])

    def test_returns_new_interval_at_beginning(self):
        """Takes in intervals + new interval and places it at beginning unmerged"""
        result = insert([[4, 5], [6, 7]], [0, 0])
        self.assertEqual(result, [[0, 0], [4, 5], [6, 7]])

    def test_returns_new_interval_at_end(self):
        """Takes in intervals + new interval and places it at end unmerged"""
        result = insert([[3, 4], [5, 6], [7, 8]], [9, 10])
        self.assertEqual(result, [[3, 4], [5, 6], [7, 8], [9, 10]])
    
    def test_returns_new_interval_in_middle(self):
        """Takes in intervals + new interval and places it in middle unmerged"""
        result = insert([[0, 0], [9, 10]], [5, 6])
        self.assertEqual(result, [[0, 0], [5, 6], [9, 10]])

    def test_merges_new_interval_and_existing_intervals(self):
        """Takes in intervals + new interval and merges them all together"""
        result = insert([[0, 3], [4, 8], [15, 16], [17, 20]], [0, 17])
        self.assertEqual(result, [[0, 20]])

    def test_merges_new_interval_at_single_point(self):
        """Takes in intervals + new interval and merges it in the correct spot"""
        result = insert([[0, 3], [5, 8], [16, 19]], [7, 10])
        self.assertEqual(result, [[0, 3], [5, 10], [16, 19]])

if __name__ == "__main__":
    unittest.main()