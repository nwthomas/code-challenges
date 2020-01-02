from singly_linked_palindrome import Node, is_palindrome
import unittest


def create_linked_list(length):
    """
    Creates a linked list of the specified length
    """
    head_node = None
    for i in range(1, length + 1):
        if head_node == None:
            head_node = Node(i)
        else:
            head_node.add_value(i)
    return head_node


class TestNode(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates a new version of the Node class
        """
        node = Node()
        self.assertIsInstance(node, Node)

    def test_instantiates_with_none(self):
        """
        Instantiates a new version of the Node class with None as the default value if no value
        is given
        """
        node = Node()
        result = node._value
        self.assertEqual(result, None)

    def test_instantiates_with_value(self):
        """
        Instantiates a new version of the Node class with a value if it is given as an argument
        """
        node = Node("test")
        result = node._value
        self.assertEqual(result, "test")

    def test_adds_value_to_list(self):
        """
        Creates a new list and successfully adds values to it
        """
        head_node = create_linked_list(10)
        result = head_node._next._next._next._next._next._value
        self.assertEqual(result, 6)

    def test_get_list_values(self):
        """
        Returns a list containing all values in the linked list
        """
        head_node = create_linked_list(10)
        result = head_node.get_list_values()
        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


class TestSinglyLinkedPalindrome(unittest.TestCase):
    def test_returns_true_if_list_is_palindrome(self):
        """
        Takes in a list as an argument and returns True if the list is a palindrome
        """
        node = Node(1)
        node.add_value(2)
        node.add_value(3)
        node.add_value(2)
        node.add_value(1)
        result = is_palindrome(node.get_list_values())
        self.assertTrue(result)

    def test_returns_false_if_list_is_not_palindrome(self):
        """
        Takes in a list as an argument and returns False if the list is not a palindrome
        """
        head_node = create_linked_list(1000)
        result = is_palindrome(head_node.get_list_values())
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
