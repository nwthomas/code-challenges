from trading_apple_stock import find_best_stock_profit
import unittest


class TestFindBestStockProfit(unittest.TestCase):
    def test_raises_typeerror_if_argument_is_not_list(self):
        """Raises a new TypeError if the argument is not of type list"""
        def result(): return find_best_stock_profit("test")
        self.assertRaises(TypeError, result)

    def test_returns_0_if_argument_is_empty_list(self):
        """Returns 0 profit if the argument is an empty list"""
        result = find_best_stock_profit([])
        self.assertEqual(result, 0)

    def test_returns_correct_profit_total(self):
        """Returns the correct profit possible from a list of stock prices"""
        result = find_best_stock_profit([10, 7, 5, 8, 11, 9])
        self.assertEqual(result, 6)

    def test_returns_correct_profit_total_from_large_list(self):
        """Returns the correct profit possible from a large list of stock prices"""
        l = [9, 10, 40, 39, 2, 45, 3, 67, 23, 10, 6, 5, 4, 4, 78, 9, 6, 100]
        result = find_best_stock_profit(l)
        self.assertEqual(result, 98)


if __name__ == "__main__":
    unittest.main()
