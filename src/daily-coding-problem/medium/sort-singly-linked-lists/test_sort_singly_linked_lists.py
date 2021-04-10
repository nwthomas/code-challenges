from sort_singly_linked_lists import Node, sort_singly_linked_lists
import unittest


class TestSortSinglyLinkedLists(unittest.TestCase):
    def create_singly_linked_list(self, values_list):
        """Creates a new SinglyLinkedList class and adds all values to it"""
        new_singly_linked_list = None

        for value in values_list:
            if not new_singly_linked_list:
                new_singly_linked_list = Node(value)
            else:
                new_singly_linked_list.add_node(value)

        return new_singly_linked_list
    
    def get_sorted_singly_linked_lists_values(self, sorted_singly_linked_list):
        """Takes in a sorted singly linked list and returns the values from it"""
        current = sorted_singly_linked_list
        final = [current.value]

        while current.next:
            current = current.next
            final.append(current.value)
        
        return final

    def test_returns_single_sorted_list(self):
        """Tests that two separate sorted singly linked lists are returned as one sorted one"""
        s1 = self.create_singly_linked_list([1, 3, 4, 6, 8, 40, 89, 28, 90, 100])
        s2 = self.create_singly_linked_list([2, 5, 8, 11, 12, 100, 567, 1000])
        s3 = self.create_singly_linked_list([1, 4, 6, 9, 10, 34, 162873, 126381672389, 123961987263])
        result = sort_singly_linked_lists(s1, s2, s3)
        self.assertEqual(self.get_sorted_singly_linked_lists_values(result), [1, 1, 2, 3, 4, 4, 5, 6, 6, 8, 8, 9, 10, 11, 12, 28, 34, 40, 89, 90, 100, 100, 567, 1000, 162873, 123961987263, 126381672389])

if __name__ == "__main__":
    unittest.main()