from last_stone_weight import last_stone_weight
import unittest

class TestLastStoneWeight(unittest.TestCase):
    def test_returns_correct_result(self):
        """Takes in an array of stones and returns the weight of the last remaining stone"""
        result = last_stone_weight([2, 3, 6, 2, 4])
        self.assertEqual(result, 1)

    def test_returns_correct_result_for_empty_array(self):
        """Takes in an empty array and returns 0"""
        result = last_stone_weight([])
        self.assertEqual(result, 0)