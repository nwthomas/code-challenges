from sort_linked_list import DoublyLinkedList, Node
import unittest


class TestNode(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates a new version of the Node class
        """
        result = Node()
        self.assertIsInstance(result, Node)

    def test_instantiates_with_none(self):
        """
        Instantiates with None as the default value if no value is given
        """
        result = Node().value
        self.assertIsNone(result)

    def test_instantiates_with_value(self):
        """
        Instantiates with a value if one is given as an argument
        """
        result = Node("test").value
        self.assertEqual(result, "test")

    def test_adds_value_to_list(self):
        """
        Adds a given value to the list successfully
        """
        node = Node(3)
        node.add_value(5)
        result = node.next_node.value
        self.assertEqual(result, 5)

    def test_adds_value_if_none_in_list(self):
        """
        Adds a given value to the list even if the list is currently empty
        """
        node = Node()
        initial_value = node.value
        node.add_value(10)
        final_value = node.value
        self.assertIsNone(initial_value)
        self.assertEqual(final_value, 10)

    def test_delete_value(self):
        """
        Removes a current Node and value from the linked list
        """
        node = Node(5)
        node.add_value(10)
        node.add_value(6)
        removed_value = node.next_node.delete()
        self.assertEqual(node.next_node.value, 6)
        self.assertEqual(node.next_node.prev_node.value, 5)
        self.assertEqual(removed_value, 10)


class TestDoublyLinkedList(unittest.TestCase):
    pass


if __name__ == "__main__":
    unittest.main()
