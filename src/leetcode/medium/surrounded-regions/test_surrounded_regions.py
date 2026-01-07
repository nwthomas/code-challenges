from surrounded_regions import surroundRegions
import unittest


class TestSurroundRegions(unittest.TestCase):
    def test_should_surround_regions(self):
        """Test that the surround regions function works"""
        board = [
            ["X", "X", "X", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "O"],
        ]
        surroundRegions(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "X"],
                ["X", "X", "X", "O"],
            ],
        )

    def test_should_not_surround_regions_on_border(self):
        """Test that the surround regions function does not surround regions on the border"""
        board = [
            ["X", "X", "X", "X"],
            ["O", "X", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "O", "X", "O"],
        ]
        surroundRegions(board)
        self.assertEqual(
            board,
            [
                ["X", "X", "X", "X"],
                ["O", "X", "O", "X"],
                ["X", "O", "O", "X"],
                ["X", "O", "X", "O"],
            ],
        )


if __name__ == "__main__":
    unittest.main()
