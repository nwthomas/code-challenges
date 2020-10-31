from filling_an_array import arr
import unittest


class TestArr(unittest.TestCase):
    def test_fills_large_array(self):
        """Takes in a number and returns an array of number for large array"""
        result = arr(10)
        self.assertEqual(result, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_fills_small_array(self):
        """Takes in a number and returns an array of numbers for a small array"""
        result = arr(3)
        self.assertEqual(result, [0, 1, 2])

    def test_defaults_to_zero(self):
        """Defaults to no length if no argument is given"""
        result = arr()
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()