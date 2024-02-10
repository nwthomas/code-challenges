"""
Build an iterator class that can intake a list of anything, iterate through them,
raise a StopIteration error when finished, and include capabilities to peak at the
next item as well as 
"""
from types import int, TypeVar, Union

T = TypeVar('T')

class Iterator:
    index: int = 0

    def __init__(self, values: T) -> None:
        self.values = values

    def __iter__(self) -> T:
        if self.index < len(self.values):
            value = self.values[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

    def peak(self) -> Union[T, None]:
        if self.index < len(self.values) - 1:
            return self.values[self.index + 1]
        else:
            None

    def restart(self) -> None:
        self.index = 0