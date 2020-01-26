from math_with_lists import Node, sum_reversed_lists
import unittest


class TestNode(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates a new version of the Node class
        """
        result = Node()
        self.assertIsInstance(result, Node)

    def test_instantiates_with_none_value(self):
        """
        Instantiates with None as the default value if no value is given
        """
        node = Node()
        result = node._value
        self.assertIsNone(result)

    def test_instantiates_with_none_next(self):
        """
        Instantiates with None as the default next node if no next Node is given
        """
        node = Node()
        result = node._next
        self.assertIsNone(result)

    def test_instantiates_with_value(self):
        """
        Instantiates with a value if one is given as an argument
        """
        node = Node("test")
        result = node._value
        self.assertEqual(result, "test")

    def test_instantiates_with_next_node(self):
        """
        Instantiates with a next Node if one is given as the second argument
        """
        next_node = Node(2)
        first_node = Node(1, next_node)
        result = first_node._next
        self.assertEqual(result, next_node)

    def test_add_values_for_short_list(self):
        """
        Adds a short number of values to a list
        """
        root_node = Node(1)
        root_node.add_value(2)
        root_node.add_value(3)
        root_node.add_value(4)
        root_node.add_value(5)
        result = root_node._next._next._next._next._value
        self.assertEqual(result, 5)


class TestSumReversedLists(unittest.TestCase):
    def test_adds_to_lists(self):
        """
        Takes in two linked lists, adds them together, and returns a reversed linked list
        """
        list_1 = Node(1)
        list_1.add_value(2)
        list_2 = Node(2)
        list_2.add_value(9)
        result = sum_reversed_lists(list_1, list_2)
        self.assertEqual(result._value, 3)
        self.assertEqual(result._next._value, 1)
        self.assertEqual(result._next._next._value, 1)


if __name__ == "__main__":
    unittest.main()
