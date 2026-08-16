import unittest

from resumable_iterator import Iterator, IteratorManager


class TestIteratorManager(unittest.TestCase):
    def test_instantiates_manager_class(self):
        """Instatiates with state"""
        iterators = [Iterator([1, 2, 3, 4])]
        state = {"index": 0, "iterators": iterators}
        IteratorManager(state)

    def test_gets_value_from_first_list(self):
        """Instantiates and returns values from first iterator"""
        iterators = [Iterator([1, 2, 3, 4]), Iterator([5, 6, 7, 8])]
        state = {"index": 0, "iterators": iterators}
        im = IteratorManager(state)
        valueOne = im.__next__()
        valueTwo = im.__next__()
        self.assertEqual(valueOne, 1)
        self.assertEqual(valueTwo, 2)

    def test_starts_from_second_list(self):
        """Instantiates and starts from second iterator in state"""
        iterators = [Iterator([1, 2, 3, 4]), Iterator([5, 6, 7, 8])]
        iterators[0].index = 4
        state = {"index": 0, "iterators": iterators}
        im = IteratorManager(state)
        valueOne = im.__next__()
        valueTwo = im.__next__()
        valueThree = im.__next__()
        valueFour = im.__next__()
        self.assertEqual(valueOne, 5)
        self.assertEqual(valueTwo, 6)
        self.assertEqual(valueThree, 7)
        self.assertEqual(valueFour, 8)

        def raise_exception():
            im.__next__()

        with self.assertRaises(StopIteration):
            raise_exception()

    def test_iterators_across_iterators(self):
        """Takes in multiple iterators and iterators across them"""
        iterators = [Iterator([1, 2, 3, 4]), Iterator([5, 6, 7, 8])]
        state = {"index": 0, "iterators": iterators}
        im = IteratorManager(state)
        valueOne = im.__next__()
        valueTwo = im.__next__()
        valueThree = im.__next__()
        valueFour = im.__next__()
        valueFive = im.__next__()
        self.assertEqual(valueOne, 1)
        self.assertEqual(valueTwo, 2)
        self.assertEqual(valueThree, 3)
        self.assertEqual(valueFour, 4)
        self.assertEqual(valueFive, 5)

    def test_iterators_can_stop_and_resume(self):
        """Allows both stopping (getting) and resuming (setting) state"""
        iterators = [Iterator([1, 2, 3, 4]), Iterator([5, 6, 7, 8])]
        state = {"index": 0, "iterators": iterators}
        im = IteratorManager(state)
        valueOne = im.__next__()
        self.assertEqual(valueOne, 1)

        state = im.getState()
        resumedIm = IteratorManager({"index": 0, "iterators": []})
        resumedIm.setState(state)
        valueTwo = resumedIm.__next__()
        valueThree = resumedIm.__next__()
        valueFour = resumedIm.__next__()
        valueFive = resumedIm.__next__()
        self.assertEqual(valueTwo, 2)
        self.assertEqual(valueThree, 3)
        self.assertEqual(valueFour, 4)
        self.assertEqual(valueFive, 5)

    def test_works_well_with_loops(self):
        """Allows iteratoring with a loop"""
        iterators = [Iterator([1, 2, 3, 4]), Iterator([5, 6, 7, 8])]
        state = {"index": 0, "iterators": iterators}
        im = IteratorManager(state)

        result = []
        for val in im:
            result.append(val)

        self.assertEqual(result, [1, 2, 3, 4, 5, 6, 7, 8])


class TestIterator(unittest.TestCase):
    def test_iterates_on_int_list(self):
        """Takes in a list of ints and iterates on them"""
        l = [1, 2, 3, 4, 5]
        iterator = Iterator(l)

        for i, val in enumerate(iterator):
            self.assertEqual(val, i + 1)

    def test_iterates_on_function_list(self):
        """Takes in a list of functions and iterates on them"""
        l = [print, min, max]
        iterator = Iterator(l)

        for i, val in enumerate(iterator):
            self.assertEqual(val, l[i])

    def test_iterator_raises_stop_exception(self):
        """Takes in a list of values, iterates on them, and raises StopException"""
        l = ["test1", "test2"]
        iterator = Iterator(l)

        for _ in iterator:
            pass

        def raise_exception():
            iterator.__next__()

        with self.assertRaises(StopIteration):
            raise_exception()

    def test_iteator_peaks(self):
        """Allows peaking at next value if available, else returns None"""
        l = [1, 2, 3, 4, 5]
        iterator = Iterator(l)

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
        iterator = Iterator(l)

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
