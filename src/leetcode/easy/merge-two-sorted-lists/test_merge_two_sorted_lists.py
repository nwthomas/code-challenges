from typing import List
from merge_two_sorted_lists import merge_two_lists, ListNode
import unittest

class TestMergeTwoLists(unittest.TestCase):
    def test_returns_first_list_if_second_is_none(self):
        """Takes in a valid list and None as second list value and returns first list"""
        list = ListNode(1)
        list.next = ListNode(2)
        list.next.next = ListNode(3)

        result = merge_two_lists(list, None)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)

    def test_returns_second_list_if_first_is_none(self):
        """Takes in a valid list as second list and None for first and returns second list"""
        list = ListNode(1)
        list.next = ListNode(2)
        list.next.next = ListNode(3)

        result = merge_two_lists(None, list)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)

    def test_returns_none_for_no_lists(self):
        """Returns None if neither list is valid"""
        result = merge_two_lists(None, None)
        self.assertIsNone(result)

    def test_merges_two_lists(self):
        """Takes in two lists and merges them"""
        list1 = ListNode(1)
        list1.next = ListNode(2)
        list1.next.next = ListNode(5)

        list2 = ListNode(2)
        list2.next = ListNode(3)
        list2.next.next = ListNode(4)

        result = merge_two_lists(list1, list2)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 2)
        self.assertEqual(result.next.next.next.val, 3)
        self.assertEqual(result.next.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.next.val, 5)


if __name__ == "__main__":
    unittest.main()