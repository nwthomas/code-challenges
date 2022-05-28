from spiral_matrix import spiral_order
import unittest

class TestSpiralOrder(unittest.TestCase):
    def test_outputs_list_of_one(self):
        """Takes in a list with one array of one integer and returns it"""
        result = spiral_order([[0]])
        self.assertEqual(result, [0])

    def test_returns_correct_spiral_order(self):
        """Takes in a 2D matrix and returns a list with the integers in spiral order"""
        result = spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        self.assertEqual(result, [1, 2, 3, 6, 9, 8, 7, 4, 5])

if __name__ == "__main__":
    unittest.main()