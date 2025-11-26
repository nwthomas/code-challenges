from non_cyclical_number import isHappyNumber
import unittest

class TestIsHappyNumber(unittest.TestCase):
    def test_returns_true_for_happy_number(self):
        """Returns True if the number is a happy number"""
        result = isHappyNumber(100)
        self.assertTrue(result)

    def test_returns_false_for_non_happy_number(self):
        """Returns False if the number is not a happy number"""
        result = isHappyNumber(101)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()