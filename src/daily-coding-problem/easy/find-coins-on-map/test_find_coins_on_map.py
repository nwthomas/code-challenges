from find_coins_on_map import find_closest_coin
import unittest


class TestFindCoinsOnMap(unittest.TestCase):
    def test_throws_typeerror_for_first_argument(self):
        """Throws a new TypeError if the first argument is not of type tuple"""
        def result(): return find_closest_coin("test", [(0, 0)])
        self.assertRaises(TypeError, result)

    def test_throws_typeerror_for_second_argument(self):
        """Throws a new TypeError if the first argument is not of type list"""
        def result(): return find_closest_coin((0, 0), "test")
        self.assertRaises(TypeError, result)

    def test_find_small_distance(self):
        """Takes in a small board of coins and returns the closest coin"""
        result = find_closest_coin((0, 2), [(0, 4), (1, 0), (2, 0), (3, 2)])
        self.assertEqual(result, (0, 4))

    def test_find_large_distance(self):
        """Takes in a large board of coins and returns the closest coin"""
        result = find_closest_coin((0, 0),
                                   [(5, 6), (3, 9), (0, 10), (4, 7), (9, 2), (4, 2), (10, 0)])
        self.assertEqual(result, (4, 2))


if __name__ == "__main__":
    unittest.main()
