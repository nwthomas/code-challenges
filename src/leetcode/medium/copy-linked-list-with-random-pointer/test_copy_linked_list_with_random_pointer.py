from copy_linked_list_with_random_pointer import copyRandomList, Node
import unittest

class TestCopyLinkedListWithRandomPointer(unittest.TestCase):
    def test_copy_linked_list_with_random_pointer(self):
        """Can copy a linked list with random pointers"""
        head = Node(1)
        head.next = Node(2)
        head.next.next = Node(3)
        head.next.next.next = Node(4)
        head.next.next.next.next = Node(5)
        head.random = head.next.next
        head.next.random = head.next.next.next
        head.next.next.random = head.next.next.next.next
        head.next.next.next.random = None

        result = copyRandomList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next.val, 2)
        self.assertEqual(result.next.next.val, 3)
        self.assertEqual(result.next.next.next.val, 4)
        self.assertEqual(result.next.next.next.next.val, 5)
        self.assertEqual(result.random.val, 3)
        self.assertEqual(result.next.random.val, 4)
        self.assertEqual(result.next.next.random.val, 5)
        self.assertEqual(result.next.next.next.random, None)

    def test_copy_linked_list_with_random_pointer_empty(self):
        """Can copy an empty linked list"""
        result = copyRandomList(None)
        self.assertEqual(result, None)

    def test_copy_linked_list_with_random_pointer_single_node(self):
        """Can copy a linked list with a single node"""
        head = Node(1)
        result = copyRandomList(head)
        self.assertEqual(result.val, 1)
        self.assertEqual(result.next, None)
        self.assertEqual(result.random, None)

if __name__ == "__main__":
	unittest.main()