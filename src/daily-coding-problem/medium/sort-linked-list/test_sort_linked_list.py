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

    def test_returns_true_when_value_is_added(self):
        """
        Returns a True boolean if a new value is added to the list
        """
        node = Node(9)
        result = node.add_value(1)
        self.assertTrue(result)

    def test_returns_false_when_value_is_not_added(self):
        """
        Returns a False boolean if a new value is not added to the list
        """
        node = Node(10)
        result = node.add_value()
        self.assertFalse(result)

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
    def test_istantiates(self):
        """
        Instantiates a new version of the DoublyLinkedList class
        """
        result = DoublyLinkedList()
        self.assertIsInstance(result, DoublyLinkedList)

    def test_instantiates_with_none_head_and_tail(self):
        """
        Instantiates with None as the value for head and tail if not value is given
        """
        dll = DoublyLinkedList()
        head_value = dll.head
        tail_value = dll.tail
        self.assertIsNone(head_value)
        self.assertIsNone(tail_value)

    def test_instantiates_with_head_and_tail(self):
        """
        Instantiates with a head and tail Node value if a value is given on instantiation
        """
        dll = DoublyLinkedList("test")
        head_value = dll.head.value
        tail_value = dll.tail.value
        self.assertEqual(head_value, "test")
        self.assertEqual(tail_value, "test")

    def test_instantiates_with_length_0(self):
        """
        Instantiates with 0 as the length if no value is given
        """
        dll = DoublyLinkedList()
        result = dll.length
        self.assertEqual(result, 0)

    def test_instantiates_with_length_1(self):
        """
        Instantiates with length of 1 if a value is given on instantiation
        """
        dll = DoublyLinkedList(1000)
        result = dll.length
        self.assertEqual(result, 1)

    def test_add_value(self):
        """
        Adds a value correctly to the list
        """


if __name__ == "__main__":
    unittest.main()
