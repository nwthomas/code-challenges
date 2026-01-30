"""
DESCRIPTION
Implement a key-value store that can serialize multiple string key-value pairs into a single string and deserialize it back. Both keys and values can contain any characters including delimiters, newlines, and special characters. For example, serializing {"key:1": "val=ue", "k\ney": "v"} should produce a string that can be deserialized back to the exact same dictionary.

Input:
{"name": "John:Doe", "city": "New,York"}

Output:
Serialize(dict): "Serialized string"
Deserialize("Serialized string"): original dict

Explanation:
Serialization is the process of converting a dictionary into a string, and deserialization is the process of converting a string back into a dictionary.

Constraints:
Keys and values are strings that can contain any character (including delimiters, newlines, quotes)
Serialization must be reversible - deserialize(serialize(data)) == data
Must handle empty strings and empty dictionaries
"""

from typing import Optional
from unittest import result


def serialize(data: Optional[dict[str, str]]) -> str:
    result = ""

    if not data:
        return result

    for key, value in data.items():
        key_len = len(key)
        value_len = len(value)
        string = f"{key_len}:{key}:{value_len}:{value}"
        result += ":" + string if result else string

    return result


def deserialize(data: Optional[str]) -> dict[str, str]:
    result = {}

    if not data:
        return result

    i = 0
    while i < len(data) - 1:
        key_len_str = ""
        while data[i] != ":":
            key_len_str += data[i]
            i += 1
        key_len = int(key_len_str)

        i += 1
        key = data[i : i + key_len]
        i += key_len + 1

        value_len_str = ""
        while data[i] != ":":
            value_len_str += data[i]
            i += 1
        value_len = int(value_len_str)

        i += 1
        value = data[i : i + value_len]
        i += value_len + 1

        result[key] = value

    return result
