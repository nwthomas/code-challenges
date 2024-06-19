import unittest

from best_time_to_buy_and_sell_stock_ii import max_profit


class TestMaxProfit(unittest.TestCase):
    """Tests the max_profit function"""

    def test_handles_empty_list(self):
        """Handles an empty list passed in and returns 0"""
        result = max_profit([])
        self.assertEqual(result, 0)

    def test_handles_two_values(self):
        """Handles a single incrementing price set"""
        result = max_profit([0, 90])
        self.assertEqual(result, 90)

    def test_handles_multiple_buys(self):
        """Handles multiple buys throughout a week with high and low prices"""
        result = max_profit([7, 1, 5, 3, 6, 4])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
