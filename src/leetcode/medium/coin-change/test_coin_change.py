from coin_change import coin_change
import unittest

class TestCoinChange(unittest.TestCase):
    def test_returns_neg_one_if_no_change_possible(self):
        """Takes in an array of coins and a targeted amount and returns -1 if not possible"""
        result = coin_change([7, 10, 15], 5)
        self.assertEqual(result, -1)

    def test_returns_zero_if_target_is_zero(self):
        """Takes in array of coins and targeted amount of 0 and returns 0"""
        result = coin_change([1, 4, 5, 100], 0)
        self.assertEqual(result, 0)


    def test_returns_fewest_coins_for_targetd_amount(self):
        """Takes in an array of coins and a targeted amount and returns fewest coins to reach it"""
        result = coin_change([1, 3, 5, 8], 100)
        self.assertEqual(result, 14)

    def test_handles_coins_of_only_one(self):
        """Takes in a single coin in coin array and returns correct fewest coins for amount"""
        result = coin_change([1], 1000)
        self.assertEqual(result, 1000)

    def test_returns_neg_one_if_only_coins_greater_than_amount(self):
        """Takes in an array of coins greater than amount and returns -1 as result"""
        result = coin_change([1000, 10000], 10)
        self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()