import unittest
from tribonacci_sequence import tribonacci


class Test(unittest.TestCase):
    def test_tribonacci_sequence(self):
        self.assertEqual(tribonacci([1, 1, 1], 10), [
                         1, 1, 1, 3, 5, 9, 17, 31, 57, 105])
        self.assertEqual(tribonacci([100, 100, 100], 3), [100, 100, 100])
        self.assertEqual(tribonacci([10, 10], 1), [10])


if __name__ == "__main__":
    unittest.main()
