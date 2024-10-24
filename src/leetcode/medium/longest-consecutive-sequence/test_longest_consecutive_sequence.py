import unittest

from longest_consecutive_sequence import (
    longest_consecutive_sequence_with_heap,
    longest_consecutive_sequence_with_set,
)


class TestLongestConsecutiveSequenceWithHeap(unittest.TestCase):
    """Tests the longest consecutive sequence with a heap function implementation"""

    def test_returns_correct_longest_consecutive_sequence_total(self):
        """Takes in an unsorted list of numbers and returns correct total"""
        result = longest_consecutive_sequence_with_heap(
            [3, 100, 4, 5, 23, 6, 19, 7])
        self.assertEqual(result, 5)

    def test_returns_zero_if_empty_list(self):
        """Takes in empty list and returns 0 for the total"""
        result = longest_consecutive_sequence_with_heap([])
        self.assertEqual(result, 0)

    def test_returns_one_for_single_number(self):
        """Takes in a list with one number and returns the correct total"""
        result = longest_consecutive_sequence_with_heap([100])
        self.assertEqual(result, 1)


class TestLongestConsecutiveWithSet(unittest.TestCase):
    """Tests the longest consecutive sequence with a set function implementation"""

    def test_returns_correct_longest_consecutive_sequence_total(self):
        """Takes in an unsorted list of numbers and returns correct total"""
        result = longest_consecutive_sequence_with_set(
            [3, 100, 4, 5, 23, 6, 19, 7])
        self.assertEqual(result, 5)

    def test_returns_zero_if_empty_list(self):
        """Takes in empty list and returns 0 for the total"""
        result = longest_consecutive_sequence_with_set([])
        self.assertEqual(result, 0)

    def test_returns_one_for_single_number(self):
        """Takes in a list with one number and returns the correct total"""
        result = longest_consecutive_sequence_with_set([100])
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
