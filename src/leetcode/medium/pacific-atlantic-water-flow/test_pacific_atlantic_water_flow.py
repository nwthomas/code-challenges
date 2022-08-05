from pacific_atlantic_water_flow import pacific_atlantic
import unittest

class TestPacificAtlantic(unittest.TestCase):
    def test_returns_correct_cells_for_small_grid(self):
        """Takes in a small grid and returns the correct cells"""
        result = pacific_atlantic([[1, 5], [5, 1]])
        self.assertEqual(result, [[0, 1], [1, 0]])

    def test_returns_correct_cells_for_large_grid(self):
        """Takes in a large grid and returns the correct cells"""
        grid = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        result = pacific_atlantic(grid)
        self.assertEqual(result, [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])

    def test_returns_all_cells_if_all_are_level(self):
        """Takes in a grid completely level and returns all cells"""
        grid = [[2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2], [2, 2, 2, 2]]
        result = pacific_atlantic(grid)
        self.assertEqual(result, [
            [0, 0], [0, 1], [0, 2], [0, 3],
            [1, 0], [1, 1], [1, 2], [1, 3],
            [2, 0], [2, 1], [2, 2], [2, 3],
            [3, 0], [3, 1], [3, 2], [3, 3],
        ])

    def test_returns_empty_list_for_empty_grid(self):
        """Takes in an empty grid and returns an empty list of results"""
        result = pacific_atlantic([])
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()