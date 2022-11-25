from valid_sedoku import isValidSudoku
import unittest

class TestIsValidSedoku(unittest.TestCase):
    invalidSedoku = [
        [".",".",".",".","5",".",".","1","."],
        [".","4",".","3",".",".",".",".","."],
        [".",".",".",".",".","3",".",".","1"],
        ["8",".",".",".",".",".",".","2","."],
        [".",".","2",".","7",".",".",".","."],
        [".","1","5",".",".",".",".",".","."],
        [".",".",".",".",".","2",".",".","."],
        [".","2",".","9",".",".",".",".","."],
        [".",".","4",".",".",".",".",".","."],
    ]

    validSedoku = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    def test_is_valid_sedoku(self):
        """Takes in a sedoku puzzle and returns True if it's valid"""
        result = isValidSudoku(self.validSedoku)
        self.assertTrue(result)

    def test_is_invalid_sedoku(self):
        """Takes in a sedoku puzzle and returns False if it's invalid"""
        result = isValidSudoku(self.invalidSedoku)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()