from walls_and_grapes import wallsAndGrapes
import unittest


class TestWallsAndGrapes(unittest.TestCase):
    def test_sets_correct_values_for_small_grid(self):
        """Sets the correct values for a small grid"""
        grid = [
            [-1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647],
        ]
        wallsAndGrapes(grid)
        self.assertEqual(
            grid,
            [
                [-1, 0, 1],
                [2, 1, 2],
            ],
        )

    def test_sets_correct_values_for_large_grid(self):
        """Sets the correct values for a large grid"""
        grid = [
            [-1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647],
            [-1, 2147483647, 2147483647],
            [0, -1, 2147483647],
        ]
        wallsAndGrapes(grid)
        self.assertEqual(
            grid,
            [
                [-1, 0, 1],
                [2, 1, 2],
                [-1, 2, 3],
                [0, -1, 4],
            ],
        )

    def test_leaves_impossible_cells_set_to_inf(self):
        """Leaves impossible cells set to inf"""
        grid = [
            [0, -1, 2147483647],
            [2147483647, -1, -1],
        ]
        wallsAndGrapes(grid)
        self.assertEqual(
            grid,
            [
                [0, -1, 2147483647],
                [1, -1, -1],
            ],
        )


if __name__ == "__main__":
    unittest.main()
