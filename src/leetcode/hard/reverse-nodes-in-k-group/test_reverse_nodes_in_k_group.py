from reverse_nodes_in_k_group import reverseKGroup, ListNode
from typing import List
import unittest


def get_list_values(head: ListNode) -> List[int]:
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


class TestReverseNodesInKGroup(unittest.TestCase):
    def test_reverse_nodes_in_k_group(self):
        """Tests that the function reverses the nodes in the list in groups of k"""
        head = ListNode(
            1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))
        )
        result = reverseKGroup(head, 3)
        result_values = get_list_values(result)
        self.assertEqual(result_values, [3, 2, 1, 6, 5, 4])

    def test_reverse_nodes_in_k_group_with_less_than_k_nodes(self):
        """Tests that the function returns the original list if the number of nodes is less than k"""
        head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = reverseKGroup(head, 3)
        result_values = get_list_values(result)
        self.assertEqual(result_values, [3, 2, 1, 4, 5])

    def test_returns_root_if_only_one_node(self):
        """Tests that the function returns the root node if there is only one node"""
        head = ListNode(1)
        result = reverseKGroup(head, 1)
        result_values = get_list_values(result)
        self.assertEqual(result_values, [1])


if __name__ == "__main__":
    unittest.main()
