"""
Write a class called Spreadsheet that will write (put) and obtain (get) values from a table
like in Excel. You can assume that values accessed will exist, but we may want to create a
caching system in order to avoid multiple highly intensive computational actions.
"""

class Spreadsheet:
    def __init__(self):
        self.cells = []
        self.cache = []
        self.graph = []

    def put(self, key: str, value: str) -> None:
        # if key in self.cells:
        #     self.recursively_clear_cache(key)

        self.cells[key] = value

    def get(self, key: str) -> str:
        # if key in self.cache:
        #     return self.cache[key]
    
        value = self.cells[key]

        if int(value) == float("nan"):
            total = 0
            split_values = value[1:].split("+")
        else:
            return value



    def recursively_clear_cache(self, key: str) -> None:
        pass
