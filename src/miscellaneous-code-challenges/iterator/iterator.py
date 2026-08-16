"""
Build an iterator class that can intake a list of anything, iterate through them,
raise a StopIteration error when finished, and include capabilities to peak at the
next item as well as 
"""

type State = dict[str, list["Iterator"] | int]


class IteratorManager[T]:
    state: State
    # {
    #   iterators: list[<iterator class>],
    #   index: int,
    # }

    def __init__(self, state: State):
        self.state = state

    def __iter__(self) -> IteratorManager:
        return self

    def __next__(self) -> T:
        currentIndex = self.state["index"]
        iterators = self.state["iterators"]
        if currentIndex >= len(iterators):
            raise StopIteration

        currentIterator = self.state["iterators"][currentIndex]
        if currentIterator.index < len(currentIterator.values):
            return currentIterator.__next__()

        self.state["index"] += 1
        if self.state["index"] >= len(iterators):
            raise StopIteration

        currentIndex = self.state["index"]
        currentIterator = self.state["iterators"][currentIndex]
        return currentIterator.__next__()

    def getState(self) -> State:
        return self.state

    def setState(self, state: State):
        self.state = state


class Iterator[T]:
    index: int = 0
    values: list[T]

    def __init__(self, values: list[T]) -> None:
        self.values = values

    def __iter__(self) -> Iterator:
        return self

    def __next__(self) -> T:
        if self.index < len(self.values):
            value = self.values[self.index]
            self.index += 1
            return value

        raise StopIteration

    def peak(self) -> T | None:
        if self.index < len(self.values) - 1:
            return self.values[self.index + 1]

        return None

    def restart(self) -> None:
        self.index = 0
