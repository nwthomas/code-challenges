import unittest

from min_cost_climbing_stairs import get_min_cost_climbing_stairs


class TestGetMinCostClimbingStairs(unittest.TestCase):
    def test_returns_minimum_cost_for_small_staircase(self):
        """Tests that the function returns the minimum cost for climbing a small staircase"""
        staircase_costs = [0, 3, 10, 8, 2, 1, 7]
        result = get_min_cost_climbing_stairs(staircase_costs)
        self.assertEqual(result, 12)

    def test_returns_minimum_cost_for_large_staircase(self):
        """Tests that the function returns the minimum cost for climbing a large staircase"""
        staircase_costs = [10, 1, 30, 4, 8, 26, 7,
                           45, 81, 10, 0, 4, 67, 10, 9, 7, 3, 1]
        result = get_min_cost_climbing_stairs(staircase_costs)
        self.assertEqual(result, 97)

    def test_gracefully_handles_empty_staircase(self):
        """Returns 0 if the staircase list is empty"""
        staircase_costs = []
        result = get_min_cost_climbing_stairs(staircase_costs)
        self.assertEqual(result, 0)

    def test_gracefully_handles_staircase_of_length_one(self):
        """Handles a staircase of length and cost length 1"""
        staircase_costs = [10]
        result = get_min_cost_climbing_stairs(staircase_costs)
        self.assertEqual(result, 10)


if __name__ == "__main__":
    unittest.main()
