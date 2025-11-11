from koko_eating_bananas import min_eating_speed
import unittest

class TestMinEatingSpeed(unittest.TestCase):
    def test_eats_small_piles_with_large_hours(self):
        """Tests that the function returns the minimum eating speed for small piles with large hours"""
        result = min_eating_speed([3, 6, 7, 11], 10)
        self.assertEqual(result, 3)

    def test_eats_large_piles_with_small_hours(self):
        """Tests that the function returns the minimum eating speed for large piles with small hours"""
        result = min_eating_speed([30, 11, 23, 4, 20], 5)
        self.assertEqual(result, 30)

    def test_eats_large_piles_with_large_hours(self):
        """Tests that the function returns the minimum eating speed for large piles with large hours"""
        result = min_eating_speed([30, 24, 23, 10, 9], 100)
        self.assertEqual(result, 1)

    def test_eats_large_piles_with_small_hours(self):
        """Tests that the function returns the minimum eating speed for large piles with small hours"""
        result = min_eating_speed([30, 24, 23, 10, 9], 5)
        self.assertEqual(result, 30)

if __name__ == "__main__":
    unittest.main()