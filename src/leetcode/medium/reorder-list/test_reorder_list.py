from reorder_list import ListNode, reorder_list
import unittest
from typing import List

class TestReorderList(unittest.TestCase):
    def is_correct_order(self, root_node: ListNode, order: List):
        current = root_node

        for num in order:
            if current.val != num:
                return False
            else:
                current = current.next

        return True

    def test_reorders_short_list(self):
        """Takes in a short list and reoders it"""
        root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = reorder_list(root)
        self.assertTrue(self.is_correct_order(result, [1, 4, 2, 3]))

    def test_reorders_long_list(self):
        """Takes in a long list and reorders it"""
        root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8))))))))
        result = reorder_list(root)
        self.assertTrue(self.is_correct_order(result, [1, 8, 2, 7, 3, 6, 4, 5]))


if __name__ == "__main__":
    unittest.main()