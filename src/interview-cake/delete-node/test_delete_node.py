from delete_node import delete_node, SinglyLinkedList
import unittest

class TestDeleteNode(unittest.TestCase):
    def test_deletes_node(self):
        """Tests that a node is successfully deleted"""
        sll = self.create_singly_linked_list([3, 5, 7])
        self.assertEqual(sll.head.next.value, 5)

        node_to_delete = sll.head.next
        delete_node(node_to_delete)

        self.assertEqual(sll.head.next.value, 7)

    def test_raises_error_if_end_node(self):
        sll = self.create_singly_linked_list([3, 5, 7])
        node_to_delete = sll.head.next.next

        def result(): return delete_node(node)
        self.assertRaises(Exception, result)
    
    def create_singly_linked_list(self, l):
        """Creates a singly linked list for testing purposes"""
        sll = SinglyLinkedList()

        for index in range(0, len(l)):
            sll.add_node_to_list(l[index])
        
        return sll
        

if __name__ == "__main__":
    unittest.main()