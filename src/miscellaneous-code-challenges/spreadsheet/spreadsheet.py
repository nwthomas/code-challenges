"""
Write a class called Spreadsheet that will write (put) and obtain (get) values from a table
like in Excel. You can assume that values accessed will exist, but we may want to create a
caching system in order to avoid multiple highly intensive computational actions.
"""

from collections import defaultdict


class Spreadsheet:
    def __init__(self):
        self.cells = {}
        self.cache = {}
        self.childToParents = defaultdict(list)

    def put(self, key: str, value: str) -> None:
        self.cells[key] = value
        self.recursivelyClearCache(key)

    def get(self, key: str, visited=None) -> int:
        if key in self.cache:
            return self.cache[key]
        if not visited:
            visited = set()
        if key in visited:
            raise ValueError("Cycle detected")

        visited.add(key)

        value = self.cells[key]

        total = 0
        if self.isNumber(value):
            return int(value)

        valueList = value[1:].split("+")
        for v in valueList:
            if self.isNumber(v):
                total += int(v)
            else:
                self.childToParents[v].append(key)
                total += self.get(v, visited.copy())

        self.cache[key] = total

        return total

    def isNumber(self, value: str) -> bool:
        try:
            int(value)
            return True
        except:
            return False

    def recursivelyClearCache(self, key: str):
        if key in self.cache:
            del self.cache[key]

        parents = self.childToParents[key]
        if len(parents) == 0:
            return

        for p in parents:
            self.recursivelyClearCache(p)

        self.childToParents[key] = []
