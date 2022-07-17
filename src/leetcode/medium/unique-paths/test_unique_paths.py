from unique_paths import unique_paths
import unittest

class TestUniquePaths(unittest.TestCase):
    def test_handles_one_and_one(self):
        """Takes in m = 1 and n = 1 and returns 1"""
        result = unique_paths(1, 1)
        self.assertEqual(result, 1)

    def test_handles_tall_matrix(self):
        """Takes in a tall 2D matrix and returns the correct possible paths"""
        result = unique_paths(100, 4)
        self.assertEqual(result, 171700)

    def test_handles_wide_matrix(self):
        """Takes in a wide 2D matrix and returns the correct possible paths"""
        result = unique_paths(4, 100)
        self.assertEqual(result, 171700)

if __name__ == "__main__":
    unittest.main()