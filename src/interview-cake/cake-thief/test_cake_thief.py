from webbrowser import get
from cake_thief import get_max_cake_value
import unittest

class TestGetMaxCakeValue(unittest.TestCase):
    cakes = [
            { "weight": 7, "value": 160 },
            { "weight": 3, "value": 90 },
            { "weight": 2, "value": 15 },
        ]

    def test_returns_correct_max_value(self):
        """Takes in a list of cakes and capacity and returns correct max value"""
        result = get_max_cake_value(self.cakes, 20)
        self.assertEqual(result, 555)

    def test_handles_zero_capacity(self):
        """Handles situations when the duffel size is 0"""
        result = get_max_cake_value(self.cakes, 0)
        self.assertEqual(result, 0)

    def test_handles_zero_weight_zero_value(self):
        """Handles situations where the cake is { weight: 0, value: 0 }"""
        cakes = [
            { "weight": 7, "value": 160 },
            { "weight": 3, "value": 90 },
            { "weight": 2, "value": 15 },
            { "weight": 0, "value": 0 },
        ]

        result = get_max_cake_value(cakes, 20)
        self.assertEqual(result, 555)

if __name__ == "__main__":
    unittest.main()