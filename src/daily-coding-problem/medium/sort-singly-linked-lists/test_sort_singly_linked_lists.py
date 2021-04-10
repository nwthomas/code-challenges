from sort_singly_linked_lists import SinglyLinkedList, quick_sort_singly_linked_lists
import unittest


class TestSortSinglyLinkedLists(unittest.TestCase):
    def create_singly_linked_list(self, values_list):
        """Creates a new SinglyLinkedList class and adds all values to it"""
        new_singly_linked_list = None

        for value in values_list:
            if not new_singly_linked_list:
                new_singly_linked_list = SinglyLinkedList(value)
            else:
                new_singly_linked_list.add_node(value)

        return new_singly_linked_list

    def test_returns_sorted_list(self):
        """Tests that two separate sorted singly linked lists are returned as one sorted one"""
        s1 = self.create_singly_linked_list([1, 3, 4, 6, 8])
        s2 = self.create_singly_linked_list([2, 5, 8, 11, 12])
        print(quick_sort_singly_linked_lists(s1, s2).head)

if __name__ == "__main__":
    unittest.main()