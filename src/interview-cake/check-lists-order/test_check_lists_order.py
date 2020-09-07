from check_lists_order import check_cake_order_sequence
import unittest


class TestCheckCakeOrderSequence(unittest.TestCase):
    def test_returns_true_if_served_orders_are_sequential(self):
        """Returns a True boolean if all the served orders are sequential"""
        result = check_cake_order_sequence(
            [6, 3, 5], [10, 1], [10, 6, 3, 1, 5])
        self.assertTrue(result)

    def test_returns_false_if_served_orders_are_not_sequential(self):
        """Returns a False boolean if all the served orders are not sequential"""
        result = check_cake_order_sequence(
            [1, 2, 3], [4, 5, 6], [6, 1, 3, 4, 52])
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
