"""
Write a class called Spreadsheet that will write (put) and obtain (get) values from a table
like in Excel. You can assume that values accessed will exist, but we may want to create a
caching system in order to avoid multiple highly intensive computational actions.
"""

class Spreadsheet:
    def __init__(self):
        self.cells = {}
        self.cache = {}
        self.graph = {}

    def put(self, key: str, value: str) -> None:
        if key in self.cells:
            self.recursively_clear_cache(key)

        self.cells[key] = value

    def get(self, key: str) -> str:
        if key in self.cache:
            return self.cache[key]
    
        cell_value = self.cells[key]

        if cell_value[0] == "=":
            total = 0
            split_values = cell_value[1:].split("+")

            for value in split_values:
                total += int(value) if self.is_int(value) else self.get(value)

            return total
        else:
            return cell_value

    def recursively_clear_cache(self, key: str) -> None:
        pass

    def is_int(self, string: str) -> bool:
        try: 
            int(string)
        except ValueError:
            return False
        else:
            return True
