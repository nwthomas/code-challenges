from typing import List
from linked_list_cycle import has_cycle, ListNode
import unittest

class TestHasCycle(unittest.TestCase):
    def test_returns_false_for_no_cycle(self):
        """Takes in a SLL and returns False if no cycle"""
        sll = ListNode(1)
        sll.next = ListNode(2)
        sll.next.next = ListNode(3)
        sll.next.next.next = ListNode(4)

        result = has_cycle(sll)
        self.assertFalse(result)

    def test_returns_true_for_cycle(self):
        """Takes in a SLL and returns True if cycle"""
        sll = ListNode(1)
        sll.next = ListNode(2)
        sll.next.next = ListNode(3)
        sll.next.next.next = ListNode(4)
        sll.next.next.next.next = sll.next

        result = has_cycle(sll)
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()