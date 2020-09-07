from merge_meeting_ranges import merge_meeting_ranges, merge_sort, merge
import unittest


class TestMerge(unittest.TestCase):
    def test_merged_lists(self):
        """Returns two lists of tuples sorted and merged together"""
        result = merge([(1, 10)], [(3, 5)])
        self.assertEqual(result, [(1, 10), (3, 5)])


class TestMergSort(unittest.TestCase):
    def test_returns_list_of_one_tuple(self):
        """Returns a list of one tuple quickly"""
        result = merge_sort([(3, 6)])
        self.assertEqual(result, [(3, 6)])

    def test_merge_sorts_list_of_tuples(self):
        """Returns merge sorted list of tuples"""
        l = [(1, 2), (4, 8), (2, 5), (1, 10)]
        result = merge_sort(l)
        self.assertEqual(result, [(1, 10), (1, 2), (2, 5), (4, 8)])


class TestMergedMeetingRange(unittest.TestCase):
    def test_returns_empty_list(self):
        """Returns an empty list if the argument is passed in"""
        result = merge_meeting_ranges([])
        self.assertEqual(result, [])

    def test_raises_exception_for_wrong_type(self):
        """Raises a TypeError if the argument is not of type list"""
        def result(): return merge_meeting_ranges("test")
        self.assertRaises(TypeError, result)

    def test_returns_two_meetings_merged(self):
        """Merges two overlapping meetings together"""
        result = merge_meeting_ranges([(1, 3), (2, 10)])
        self.assertEqual(result, [(1, 10)])


if __name__ == "__main__":
    unittest.main()
