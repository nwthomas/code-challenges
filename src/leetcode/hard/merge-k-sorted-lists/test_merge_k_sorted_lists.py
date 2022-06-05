from merge_k_sorted_lists import merge_k_lists, ListNode
import unittest

class TestMergeKLists(unittest.TestCase):
    short_list = ListNode(1)
    short_list.next = ListNode(2)
    short_list.next.next = ListNode(3)

    long_list = ListNode(1)
    long_list.next = ListNode(2)
    long_list.next.next = ListNode(3)
    long_list.next.next.next = ListNode(4)
    long_list.next.next.next.next = ListNode(5)
    long_list.next.next.next.next.next = ListNode(6)

    def test_merges_lists(self):
        """Takes in two SLL and merges them together"""
        result = merge_k_lists([self.short_list, self.long_list])
        answers = [1, 1, 2, 2, 3, 3, 4, 5, 6]

        current = result
        i = 0

        while current:
            self.assertEqual(current.val, answers[i])
            i += 1
            current = current.next

    def test_returns_none_for_no_singly_linked_lists(self):
        """Returns None if there are no SLLs in input list"""
        result = merge_k_lists([])
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()