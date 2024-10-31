import unittest

from trapping_rain_water import trap


class TestTrap(unittest.TestCase):
    def test_returns_zero_if_empty_list(self):
        """Takes in an empty list and returns 0"""
        result = trap([])
        self.assertEqual(result, 0)

    def test_throws_typeerror_if_arguments_not_list(self):
        """Takes in an argument of not a list and raises a TypeError"""
        def result():
            return trap("test")

        self.assertRaises(TypeError, result)

    def test_returns_zero_for_flat_levels(self):
        """Takes in a list of 0s and returns 0"""
        result = trap([0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(result, 0)

    def test_returns_trapped_rainwater_for_end_caps(self):
        """Takes in a list with two end pillars and returns trapped water"""
        result = trap([10, 0, 0, 0, 0, 0, 0, 0, 0, 10])
        self.assertEqual(result, 80)

    def test_returns_trapped_rainwater_for_variable_list(self):
        """Takes in a list with variable numbers and returns trapped water"""
        result = trap([4, 2, 0, 3, 2, 5])
        self.assertEqual(result, 9)


if __name__ == "__main__":
    unittest.main()
