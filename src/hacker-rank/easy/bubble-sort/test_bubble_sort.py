from itertools import count
from bubble_sort import countSwaps
import unittest

class TestCountSwaps(unittest.TestCase):
    def test_sorts_and_counts(self):
        """Sorts and counts the number of swaps"""
        [numSwaps, first, last] = countSwaps([6, 4, 1])
        self.assertEqual(numSwaps, 3)
        self.assertEqual(first, 1)
        self.assertEqual(last, 6)

    def test_returns_zero(self):
        """Prints 0 if no swaps are required"""
        [numSwaps, first, last] = countSwaps([0, 1, 2, 3, 4, 5])
        self.assertEqual(numSwaps, 0)
        self.assertEqual(first, 0)
        self.assertEqual(last, 5)

if __name__ == "__main__":
    unittest.main()