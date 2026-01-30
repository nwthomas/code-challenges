"""
Problem
Implement a simple in-memory database for one table. All values are strings.
Each row is identified by a rowKey (string). Each row contains columns identified by colKey (string).
You must process a sequence of commands and output results for read/query commands.

Supported commands
- SET rowKey colKey value
    - Set table[rowKey][colKey] = value
- GET rowKey colKey
    - Output the value if present, otherwise output NULL
- SELECT whereCol whereValue orderByCol
    - Return all rowKeys for rows where table[rowKey][whereCol] == whereValue
    - Sort the matching rows by the value of orderByCol in ascending lexicographic order
    - If a row is missing orderByCol, treat its sort value as an empty string ""
    - If multiple rows have the same orderByCol value, break ties by rowKey ascending
    - Output the resulting rowKey s joined by a single space (or output an empty line if none)

nput/Output format
Input:
- list of commands (one per line).
Output:
- For each GET , print a single line.
- For each SELECT , print a single line.I

Constraints (assume)
- Up to 2 × 10^5 commands.
- Total length of all strings is within reasonable memory limits.
"""

from collections import defaultdict


class InMemorySQLTable:
    def __init__(self):
        self.table = {}

    def query(self, command: str) -> str:
        """Processes a command and returns the result."""
        command_parts = command.split(" ")

        if command_parts[0] == "SET":
            return self._set(command_parts[1:])
        if command_parts[0] == "GET":
            return self._get(command_parts[1:])
        if command_parts[0] == "SELECT":
            return self._select(command_parts[1:])

    def _set(self, command: list[str]) -> str:
        """Sets a value for a given row and column."""
        if not command[0] in self.table:
            self.table[command[0]] = {}

        self.table[command[0]][command[1]] = command[2]

    def _get(self, command: list[str]) -> str:
        """Gets a value for a given row and column. Returns 'NULL' if the value is not present."""
        if not command[0] in self.table or not command[1] in self.table[command[0]]:
            return "NULL"

        return self.table[command[0]][command[1]]

    def _select(self, command: list[str]) -> str:
        where_col = command[0]
        where_value = command[2].split("=")[1]
        order_by_col = command[5] if len(command) > 3 else ""
        order_direction = command[6] if len(command) > 3 else ""

        result = []
        for row_key, row_value in self.table.items():
            if where_col in row_value and row_value[where_col] == where_value:
                result.append({**self.table[row_key], "id": row_key})

        def sort_key(row: dict[str, str]) -> str:
            return (row[order_by_col] if order_by_col in row else "", row["id"])

        if order_by_col != "":
            if order_direction == "DESC":
                result.sort(key=sort_key, reverse=True)
            else:
                result.sort(
                    key=sort_key,
                )
        else:
            result.sort(key=lambda x: x["id"])

        return " ".join([row["id"] for row in result]) if result else ""
