from target_sum import find_target_sum_ways
import unittest

class TestFindTargetSumWays(unittest.TestCase):
    def test_returns_number_of_ways_to_reach_target(self):
        """Takes in an integer list and a target and returns the number of ways to reach it"""
        result = find_target_sum_ways([1,1,1,1,1], 3)
        self.assertEqual(result, 5)

    def test_returns_zero_if_no_ways_possible(self):
        """Takes in an integer list and a target and returns 0 if no way is possible"""
        result = find_target_sum_ways([1, 2, 3, 4, 5, 6, 7, 8, 9], 10)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()