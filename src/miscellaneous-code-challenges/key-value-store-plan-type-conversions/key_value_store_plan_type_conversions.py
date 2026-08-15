"""
Versioned key-value store: Implement a data structure with set(key, value, t) and get_at(key, t) that returns the value for key whose timestamp is the greatest <= t (or None if none).

Timestamps are integers and may arrive out of order.

Optimize both time and space for up to 1e5 keys and 1e6 operations.

Explain your data structures, complexity, and edge cases (duplicate timestamps per key, missing keys, very large t, memory).

Provide working code for core methods.
"""

from collections import defaultdict


class KeyValueStoreWithTimestamps:
    def __init__(self):
        # Store = dict{ [key: str]: list[ set(timestamp: int, value: str ) ] }
        self.store = defaultdict(list)

    def set_at(self, key: str, value: str, timestamp: int) -> None:
        i = 0
        while i < len(self.store[key]) and self.store[key][i][0] <= timestamp:
            i += 1

        self.store[key] = self.store[key][:i] + \
            [(timestamp, value)] + self.store[key][i:]

    def get_at(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        if not key in self.store or len(values) == 0:
            return ""

        left = 0
        right = len(values) - 1
        max_seen = values[0]

        while left < right:
            pivot = left + right // 2

            if pivot > len(values) - 1 or values[pivot] == max_seen:
                break

            val = values[pivot]
            if val[0] <= timestamp:
                max_seen = val
                left = pivot + 1
            else:
                right = pivot - 1

        return max_seen[1]
