from remove_nth_node_from_end_of_list import ListNode, remove_nth_from_end
import unittest

class TestRemoveNthFromEnd(unittest.TestCase):
    def get_list_values(self, root: ListNode):
        """Takes in a SLL and returns a list of the values"""
        values = []
        current = root

        while current:
            values.append(current.val)
            current = current.next

        return values

    def test_removes_node_from_short_list(self):
        """Takes in a short SLL and removes a node at nth spot"""
        root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = remove_nth_from_end(root, 2)
        result_values = self.get_list_values(result)
        self.assertEqual(result_values, [1, 2, 3, 5])

    def test_removes_node_from_long_list(self):
        """Takes in a long SLL and removes a node at nth spot"""
        root = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
        result = remove_nth_from_end(root, 9)
        result_values = self.get_list_values(result)
        self.assertEqual(result_values, [2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == "__main__":
    unittest.main()