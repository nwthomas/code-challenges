from peekable_iterator import Iterator, PeekableInterface
import unittest


class TestIterator(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates a new version of the Iterator class
        """
        iterator = Iterator(iter([1, 2, 3, 4]))
        self.assertIsInstance(iterator, Iterator)

    def test_instantiates_with_iterator(self):
        """
        Instantiates with an iterator saved to the self.iter property of the class
        """
        iterator_object = iter([1, 2, 3, 4])
        iterator = Iterator(iterator_object)
        result = iterator.iter
        self.assertEqual(result, iterator_object)

    def test_returns_next_value(self):
        """
        Returns the next value in the Iterator
        """
        iterator = Iterator(iter([1, 2, 3]))
        result = iterator.next_value()
        self.assertEqual(result, 1)

    def test_returns_true_if_has_next(self):
        """
        Returns True if there is a next value in the Iterator
        """
        iterator = Iterator(iter([1, 2, 3]))
        result = iterator.has_next()
        self.assertTrue(result)

    def test_returns_false_if_not_has_next(self):
        """
        Returns False if there is not a next value in the Iterator
        """
        iterator = Iterator(iter([]))
        result = iterator.has_next()
        self.assertFalse(result)

    def test_returns_true_if_called_twice(self):
        """
        Returns True even if it's called twice
        """
        iterator = Iterator(iter([1, 2, 3, 4]))
        iterator.has_next()
        result = iterator.has_next()
        self.assertTrue(result)

    def test_assigns_peeked_value_when_called(self):
        """
        Assigns value to peeked_value when called
        """
        iterator = Iterator(iter([1, 2, 3]))
        iterator.has_next()
        result = iterator.peeked_value
        self.assertEqual(result, 1)

    def test_returns_next_value_from_peeked_value(self):
        """
        If has_next has been called, the peeked_value is returned from the next_value
        method
        """
        iterator = Iterator(iter([1, 2, 3, 4]))
        iterator.has_next()
        result_value = iterator.next_value()
        result_peeked_value = iterator.peeked_value
        self.assertEqual(result_value, 1)
        self.assertEqual(result_peeked_value, None)


class TestPeekableInterface(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates a new version of the Peekable Iterface class
        """
        pk = PeekableInterface(iter([1, 2, 3, 4]))
        self.assertIsInstance(pk, PeekableInterface)

    def test_peeks_at_next_value(self):
        """
        Returns the next value in the iterator
        """
        pk = PeekableInterface(iter([1, 2, 3, 4]))
        result = pk.peek()
        self.assertEqual(result, 1)

    def test_returns_true_if_has_next(self):
        """
        Returns True if there is a next value available in the iterator
        """
        pk = PeekableInterface(iter([1, 2, 3, 4]))
        result = pk.has_next()
        self.assertTrue(result)

    def test_returns_false_if_not_has_next(self):
        """
        Returns False if there is not a next value available in the iterator
        """
        pk = PeekableInterface(iter([]))
        result = pk.has_next()
        self.assertFalse(result)

    def test_returns_next_value(self):
        """
        Returns the next value available in the interator
        """
        pk = PeekableInterface(iter([1, 2, 3]))
        result = pk.next_value()
        self.assertEqual(result, 1)

    def test_returns_none_if_not_next_value(self):
        """
        Returns None if there is no next value available in the interator
        """
        pk = PeekableInterface(iter([1, 2, 3]))
        pk.next_value()
        pk.next_value()
        pk.next_value()
        result = pk.next_value()
        self.assertIsNone(result)

    def test_returns_true_if_next_value(self):
        """
        Returns True if there is a next value in the iterator
        """
        pk = PeekableInterface(iter([1, 2, 3]))
        result = pk.has_next()
        self.assertTrue(result)

    def test_returns_false_if_not_next_value(self):
        """
        Returns False if there is not a nexr value in the iterator
        """
        pk = PeekableInterface(iter([]))
        result = pk.has_next()
        self.assertFalse(result)

    def test_returns_false_has_next_after_iterating(self):
        """
        Returns false from the has_next method after iterating to the end of the iterator
        """
        pk = PeekableInterface(iter([1, 2, 3]))
        pk.has_next()
        one = pk.next_value()
        two = pk.next_value()
        pk.has_next()
        three = pk.next_value()
        result = pk.has_next()
        self.assertEqual(one, 1)
        self.assertEqual(two, 2)
        self.assertEqual(three, 3)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
