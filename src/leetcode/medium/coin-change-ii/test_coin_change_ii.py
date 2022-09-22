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

    def test_raises_typeerror_for_wrong_first_argument(self):
        """Raises TypeError if first argument is not of type int"""
        def result():
            return change({}, [1, 2, 3])
        
        self.assertRaises(TypeError, result)

    def test_raises_typeerror_for_wrong_second_argument(self):
        """Raises TypeError if second argument is not of type list"""
        def result():
            return change(100, {})

        self.assertRaises(TypeError, result)

    def test_raises_typeerror_for_non_int_in_coins(self):
        """Raises TypeError for a non-int value in the coins list"""
        def result():
            return change(100, [1, 2, "test"])
        
        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()