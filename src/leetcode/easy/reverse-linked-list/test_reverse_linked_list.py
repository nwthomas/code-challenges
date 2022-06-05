from typing import List
from reverse_linked_list import ListNode, reverse_list
import unittest

class TestReverseList(unittest.TestCase):
    def test_returns_none_if_no_head_node(self):
        """Returns None if there's no head node"""
        result = reverse_list(head=None)
        self.assertIsNone(result)

    def test_reverses_linked_list(self):
        """Takes in a SLL and reverses it"""
        node_one = ListNode(1)
        node_one.next = ListNode(2)
        node_one.next.next = ListNode(3)
        node_one.next.next.next = ListNode(4)

        current = reverse_list(node_one)
        i = 4

        while current:
            node_val = current.val
            self.assertEqual(node_val, i)
            current = current.next
            i -= 1

if __name__ == "__main__":
    unittest.main()