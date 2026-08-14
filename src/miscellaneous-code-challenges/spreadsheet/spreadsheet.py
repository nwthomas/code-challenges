"""
Write a class called Spreadsheet that will write (put) and obtain (get) values from a table
like in Excel. You can assume that values accessed will exist, but we may want to create a
caching system in order to avoid multiple highly intensive computational actions.
"""

from collections import defaultdict


class Spreadsheet:
    def __init__(self):
        self.cache = {}
        self.cells = {}
        self.childToParents = defaultdict(list)

    def put(self, key: str, value: str) -> None:
        self.recursivelyClearCache(key)
        self.cells[key] = value

    def get(self, key: str, visited=None) -> int:
        if visited is None:
            visited = set()

        if key in self.cache:
            return self.cache[key]
        if self.isNumber(self.cells[key]):
            return int(self.cells[key])
        if key in visited:
            raise ValueError("Cycle detected")

        visited.add(key)
        val = self.cells[key]

        equation = val[1:].split("+")
        vals = []
        for cell in equation:
            if self.isNumber(cell):
                vals.append(int(cell))
                continue

            self.childToParents[cell].append(key)
            vals.append(self.get(cell, visited.copy()))

        result = 0
        for v in vals:
            result += v

        return result

    def recursivelyClearCache(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]

        parents = self.childToParents[key]

        if len(parents) == 0:
            return

        for p in parents:
            self.recursivelyClearCache(p)

        self.childToParents[key] = []

    def isNumber(self, val: str) -> bool:
        try:
            int(val)
            return True
        except:
            return False
