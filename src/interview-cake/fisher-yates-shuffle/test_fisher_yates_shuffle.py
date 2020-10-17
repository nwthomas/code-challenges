from fisher_yates_shuffle import shuffle
from copy import copy
import unittest


def create_tracker_dict(num_list):
    """Takes in a list and greates a tracker dictionary from it"""
    tracker = {}

    for num in num_list:
        if num in tracker:
            tracker[num] += 1
        else:
            tracker[num] = 1
    return tracker


def is_shuffled_list_complete(tracker, shuffled_list):
    """Takes in a tracker dict and a shuffled list and verifies the list is complete"""
    tracker = copy(tracker)

    for num in shuffled_list:
        if num in tracker and tracker[num] != 0:
            tracker[num] -= 1
        else:
            return False

    return True


class TestShuffle(unittest.TestCase):
    def test_raises_typeerror_for_non_list_argument(self):
        """Raises a new TypeError if the argument for shuffle is not type list"""
        def result(): shuffle("test")
        self.assertRaises(TypeError, result)

    def test_returns_input_if_length_less_than_2(self):
        """Returns the inputted integer list if the length is less than 2"""
        list_one = [1]
        shuffle(list_one)
        self.assertEqual(list_one, [1])

        list_empty = []
        shuffle(list_empty)
        self.assertEqual(list_empty, [])

    def test_returns_random_shuffle_with_all_nums_from_small_list(self):
        """Tests that a shuffled small list has all integers from original in it"""
        small_list = [8, 30, 2, 6]
        tracker = create_tracker_dict(small_list)
        shuffle(small_list)
        self.assertTrue(is_shuffled_list_complete(tracker, small_list))

    def test_returns_random_shuffle_with_all_nums_from_large_list(self):
        """Tests that a shuffled large list has all integers from the original in it"""
        large_list = [7812, 2, 5, 378, 5, 34, 90, 11, 8]
        tracker = create_tracker_dict(large_list)
        shuffle(large_list)
        self.assertTrue(is_shuffled_list_complete(tracker, large_list))


if __name__ == "__main__":
    unittest.main()
