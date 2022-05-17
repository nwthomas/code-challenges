from coin_change import coin_change
import unittest

class TestCoinChange(unittest.TestCase):
    def test_returns_neg_one_if_no_change_possible(self):
        """Takes in an array of coins and a targeted amount and returns -1 if not possible"""
        result = coin_change([7, 10, 15], 5)
        self.assertEqual(result, -1)

    def test_returns_fewest_coins_for_targetd_amount(self):
        """Takes in an array of coins and a targeted amount and returns fewest coins to reach it"""
        result = coin_change([1, 3, 5, 8], 100)
        self.assertEqual(result, 14)

if __name__ == "__main__":
    unittest.main()