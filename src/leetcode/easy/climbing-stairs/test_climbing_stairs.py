from climbing_stairs import climb_stairs
import unittest

class TestClimbStairs(unittest.TestCase):
    def test_returns_one_for_one_step(self):
        """Returns 1 for a step set of 1"""
        result = climb_stairs(1)
        self.assertEqual(result, 1)

    def test_returns_zero_for_zero_steps(self):
        """Returns 0 for a step set of 0"""
        result = climb_stairs(0)
        self.assertEqual(result, 1)

    def test_returns_correct_possible_count_of_steps(self):
        """Returns the correct count of steps to reach a step"""
        result = climb_stairs(20);
        self.assertEqual(result, 10946)

if __name__ == "__main__":
    unittest.main()