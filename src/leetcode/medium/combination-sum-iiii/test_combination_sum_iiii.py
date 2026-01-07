from combination_sum_iiii import combination_sum_4
import unittest


class TestCombinationSum4(unittest.TestCase):
    def test_returns_small_total_combination_sum_ways(self):
        """Takes in a list of numbers and a total and returns the small total ways to up to it"""
        result = combination_sum_4([1, 2], 2)
        self.assertEqual(result, 2)

    def test_returns_large_total_combination_sum_ways(self):
        """Takes in list of numbers and a total and returns the large total ways to sum up to it"""
        result = combination_sum_4([1, 2, 3, 4, 5], 10)
        self.assertEqual(result, 464)


if __name__ == "__main__":
    unittest.main()
