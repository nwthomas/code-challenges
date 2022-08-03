from number_of_islands import num_islands
import unittest

class TestNumIslands(unittest.TestCase):
    def test_returns_correct_number_of_islands(self):
        """Takes in a grid and returns the number of islands within it"""
        grid = [
            ["1", "1", "1", "0", "0"],
            ["1", "1", "0", "0", "1"],
            ["1", "0", "1", "0", "1"],
            ["0", "1", "1", "1", "1"],
            ["1", "0", "1", "1", "1"],
        ]
        result = num_islands(grid)
        self.assertEqual(result, 3)

    def test_returns_zero_for_no_islands(self):
        """Takes in a grid and returns zero if there are no islands present"""
        grid = [
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
        result = num_islands(grid)
        self.assertEqual(result, 0)

    def test_returns_zero_for_empty_grid(self):
        """Takes in an empty grid - empty list - and returns zero"""
        grid = []
        result = num_islands(grid)
        self.assertEqual(result, 0)

    def test_can_traverse_wide_grid(self):
        """Takes in a wide and short grid and returns correct island count"""
        grid = [["1", "0", "1", "1", "0", "1", "0", "0", "1", "0"]]
        result = num_islands(grid)
        self.assertEqual(result, 4)

    def test_can_traverse_tall_grid(self):
        """Takes in a tall and thin grid and returns correct island count"""
        grid = [
            ["0"],
            ["1"],
            ["1"],
            ["0"],
            ["1"],
            ["0"],
            ["1"],
            ["0"],
            ["1"],
        ]
        result = num_islands(grid)
        self.assertEqual(result, 4)

    def test_raises_typeerror_if_arg_not_list(self):
        """Takes in an argument that's not of type list and raises TypeError"""
        def result():
            return num_islands({})

        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_rows_not_list(self):
        """Takes in a list with some rows not of type list and raises TypeError"""
        def result():
            return num_islands([{}, "test", 123])

        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_cells_not_string(self):
        """Takes in a grid with some cells that aren't of type string and raises TypeError"""
        def result():
            return num_islands([["1", 2, 3], ["1", "0", {}]])

        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()