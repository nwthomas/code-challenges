from array_manipulation import array_manipulation
import unittest

class TestArrayManipulation(unittest.TestCase):
    small_query = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]
    large_query = [
        [1905427, 3813069, 86109], 
        [2620540, 3504595, 33339], 
        [4993680, 8478106, 70837],
        [3038720, 7622518, 14291],
        [1617908, 9453042, 22407],
        [1617908, 9453042, 22407],
        [642372, 9016072, 31887],
        [187355, 3576976, 6527]
    ]


    def test_completes_small_query(self):
        """Completes a small query set and returns the correct result"""
        result = array_manipulation(self.small_query)
        self.assertEqual(result, 200)

    def test_completes_large_query(self):
        """Completes a large query set and returns the correct result"""
        result = array_manipulation(self.large_query)
        self.assertEqual(result, 86109)

    def test_returns_zero_for_empty_queries(self):
        """Handles an empty queries list"""
        result = array_manipulation([])
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()