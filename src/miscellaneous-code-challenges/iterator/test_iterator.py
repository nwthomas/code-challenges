from iterator import IteratorClass
import unittest

class TestIterator(unittest.TestCase):
    def test_iterates_on_int_list(self):
        """Takes in a list of ints and iterates on them"""
        l = [1, 2, 3, 4, 5]
        iterator = IteratorClass(l)

        for i, val in enumerate(iterator):
            self.assertEqual(val, i + 1)

    def test_iterates_on_function_list(self):
        """Takes in a list of functions and iterates on them"""
        l = [print, min, max]
        iterator = IteratorClass(l)

        for i, val in enumerate(iterator):
            self.assertEqual(val, l[i])

    def test_iterator_raises_stop_exception(self):
        """Takes in a list of values, iterates on them, and raises StopException"""
        l = ["test1", "test2"]
        iterator = IteratorClass(l)

        for _ in iterator:
            pass
        
        def raise_exception():
            iterator.__next__()

        with self.assertRaises(StopIteration):
            raise_exception()

    def test_iteator_peaks(self):
        """Allows peaking at next value if available, else returns None"""
        l = [1, 2, 3, 4, 5]
        iterator = IteratorClass(l)

        next_value = iterator.peak()
        for i, _ in enumerate(iterator):
            if i < len(l) - 1:
                self.assertEqual(next_value, l[i + 1])
            else:
                self.assertIsNone(next_value)

            next_value = iterator.peak()

    def test_restarts_iterator(self):
        """Allows iteration to end of iterable and then can restart iterable class"""
        l = [print, max, min]
        iterator = IteratorClass(l)

        for _ in iterator:
            pass

        def raise_exception():
            iterator.__next__()

        with self.assertRaises(StopIteration):
            raise_exception()

        iterator.restart()

        self.assertEqual(iterator.__next__(), print)


if __name__ == "__main__":
    unittest.main()