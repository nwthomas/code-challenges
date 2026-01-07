from hand_of_straights import isNStraightHand
import unittest


class TestIsNStraightHand(unittest.TestCase):
    def test_returns_true_if_possible(self):
        """Takes in a an unsortedlist of cards with group size and returns True"""
        result = isNStraightHand([1, 8, 2, 6, 3, 4, 5, 7], 4)
        self.assertTrue(result)

    def test_returns_false_if_not_possible(self):
        """Takes in a an unsorted list of cards with group size and returns False"""
        result = isNStraightHand([1, 2, 3, 3, 4, 5, 6, 7], 4)
        self.assertFalse(result)

    def test_returns_true_if_empty_list(self):
        """Takes in an empty list and returns False"""
        result = isNStraightHand([], 4)
        self.assertTrue(result)

    def test_returns_false_if_single_card_with_large_group_size(self):
        """Takes in a list with a single card and a large group size and returns False"""
        result = isNStraightHand([1], 4)
        self.assertFalse(result)

    def test_returns_false_if_different_multiple_cards_from_group_size(self):
        """Takes in a list with multiple cards and a group size and returns False"""
        result = isNStraightHand([1, 2, 3, 4, 5, 6, 7, 8], 3)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
