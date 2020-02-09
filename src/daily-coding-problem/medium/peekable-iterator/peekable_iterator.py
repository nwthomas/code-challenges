"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface,
which also implements peek(). Peek shows the next element that would be returned on next().

Here is the interface:

class PeekableInterface(object):
    def __init__(self, iterator):
        pass

    def peek(self):
        pass

    def next(self):
        pass

    def hasNext(self):
        pass
"""


class Iterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.peeked_value = None

    def next_value(self):
        """
        Returns the next value in the iterator
        """
        if self.has_next() != None:
            temp_val = self.peeked_value
            self.peeked_value = None
            return temp_val
        else:
            return False

    def has_next(self):
        """
        Returns True if there is a next value or False otherwise
        """
        if self.peeked_value:
            return True
        else:
            temp_val = next(self.iter)
            if temp_val != None:
                self.peeked_value = temp_val
                return True
            else:
                return False


class PeekableInterface:
    def __init__(self, iterator):
        self.iter = Iterator(iterator)
        self.peeked_value = None

    def peek(self):
        """
        Returns what the next value in the iterator will be if next_value is called
        """
        if self.peeked_value:
            return self.peeked_value
        elif self.iter.has_next():
            self.peeked_value = self.iter.next_value()
            return self.peeked_value
        else:
            return None

    def next_value(self):
        """
        Returns the next value in the iterator
        """
        if self.peeked_value:
            temp_val = self.peeked_value
            self.peeked_value = None
            return temp_val
        elif self.iter.has_next():
            return self.iter.next_value()
        else:
            return None

    def has_next(self):
        """
        Returns True if there's a next value in the iterator or False otherwise
        """
        if self.peeked_value:
            return True
        elif self.iter.has_next():
            return True
        else:
            return False
