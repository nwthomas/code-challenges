import unittest
from stock_prices import find_max_profit


class Test(unittest.TestCase):
    def test_find_max_profit(self):
        self.assertEqual(find_max_profit([50, 200, 2, 54, 12, 66]), 150)
        self.assertEqual(find_max_profit([600, 100, 90, 80, 70]), -10)
        self.assertEqual(find_max_profit([100, 1]), -99)
        self.assertEqual(find_max_profit([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 8)
        self.assertEqual(find_max_profit([]), None)


if __name__ == "__main__":
    unittest.main()
