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
        self.cells[key] = value
        self.recursively_clear_cache(key)
        self.graph[key] = []

    def get(self, key: str, visited=None) -> str:
        if visited is None:
            visited = set[str]()

        if key in self.cache:
            return self.cache[key]
        if key in visited:
            raise ValueError(f"Cycle detected: {key}")

        visited.add(key)

        value = self.cells[key]
        without_equals_prefix = "".join(value.split("="))
        values_list = without_equals_prefix.split("+")

        total = 0
        for new_value in values_list:
            if new_value.isdigit():
                total += int(new_value)
            else:
                total += self.get(new_value, visited.copy())
                self.add_graph_dependency(new_value, key)

        self.cache[key] = total

        visited.remove(key)

        return total

    def recursively_clear_cache(self, key: str) -> None:
        if key in self.cache:
            del self.cache[key]

        if not key in self.graph:
            self.graph[key] = []

        for parent_dep in self.graph[key]:
            self.recursively_clear_cache(parent_dep)

    def add_graph_dependency(self, child: str, parent: str) -> None:
        if not child in self.graph:
            self.graph[child] = []

        self.graph[child].append(parent)
