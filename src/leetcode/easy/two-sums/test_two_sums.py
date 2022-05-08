from two_sums import two_sum
import unittest

class TestTwoSums(unittest.TestCase):
  def test_returns_indices(self):
    """Takes in a list of numbers and returns the targeted indices if sum is possible"""
    result = two_sum([1, 4, 6, 2, 3], 10)
    self.assertEqual(result, [1, 2])

  def test_returns_empty_list(self):
    """Returns empty list if a sum is not possible"""
    result = two_sum([1, 2, 3, 4, 5], 100)
    self.assertEqual(result, [])

if __name__ == "__main__":
  unittest.main()