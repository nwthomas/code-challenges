from escape_the_mines import find_mine_escape_path
import unittest


class TestFindMineEscapePath(unittest.TestCase):
    def test_returns_empty_list_with_empty_map(self):
        """
        Returns an empty list when the map argument is an empty list
        """
        result = find_mine_escape_path([], {"x": 1, "y": 3}, {"x": 5, "y": 1})
        self.assertEqual(result, [])

    def test_returns_correct_path_for_small_map(self):
        """
        Returns the correct path for a small map of boolean values
        """
        map = [[False, True, False], [False, True, False], [True, True, False]]
        result = find_mine_escape_path(map, {"x": 0, "y": 1}, {"x": 2, "y": 0})
        self.assertEqual(result, ["right", "right", "up"])

    def test_returns_correct_path_for_large_map(self):
        """
        Returns the correct path for a large map of boolean values
        """
        map = [[False, False, False, True, True], [True, True, True, True, False], [True, False, False, False, False], [
            True, True, True, True, True], [False, False, False, False, True], [True, True, True, True, True]]
        result = find_mine_escape_path(map, {"x": 0, "y": 4}, {"x": 5, "y": 0})
        self.assertEqual(result, ["up", "right", "up", "up", "up", "right", "right",
                                  "down", "down", "down", "down", "right", "right", "up", "up", "up", "up"])


if __name__ == "__main__":
    unittest.main()
