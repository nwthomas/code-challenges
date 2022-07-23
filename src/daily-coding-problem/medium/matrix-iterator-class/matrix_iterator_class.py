"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Implement a 2D iterator class. It will be initialized with an array of arrays, and should implement the following methods:

next(): returns the next element in the array of arrays. If there are no more elements, raise an exception.
has_next(): returns whether or not the iterator still has elements left.
For example, given the input [[1, 2], [3], [], [4, 5, 6]], calling next() repeatedly should output 1, 2, 3, 4, 5, 6.

Do not use flatten or otherwise clone the arrays. Some of the arrays can be empty.
"""

class Matrix_Iterator:
    def __init__(self, matrix):
        self.matrix = matrix
        self.y = 0
        self.x = 0
        self.next_value = None

    def next(self):
        """Returns the next iterated value in the matrix or raises exception otherwise"""
        self._get_next()

        if not self.next_value:
            raise Exception("No next value found in matrix")
        else:
            next_value = self.next_value
            self.next_value = None
            return next_value

    def has_next(self):
        """Returns True if matrix has next value or False otherwise"""
        self._get_next()

        return self.next_value is not None

    def _get_next(self):
        """Sets the next value of the matrix to self.next"""
        
        while not self.next_value and self.y < len(self.matrix):
            if self.x < len(self.matrix[self.y]):
                self.next_value = self.matrix[self.y][self.x]
                self.x += 1
            else:
                self.y += 1
                self.x = 0