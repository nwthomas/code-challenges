from typing import Type
from coin_change_ii import change
import unittest

class TestChange(unittest.TestCase):
    def test_can_find_max_change_in_small_amount(self):
        """Can return correct total ways to get to a small amount"""
        coins = [1, 3, 5, 10]
        amount = 10
        result = change(amount, coins)
        self.assertEqual(result, 8)

    def test_can_find_max_change_in_large_amount(self):
        """Can return correct total ways to get to a large amount"""
        coins = [1, 2, 4, 5, 6, 14, 15]
        amount = 100
        result = change(amount, coins)
        self.assertEqual(result, 93843)

if __name__ == "__main__":
    unittest.main()