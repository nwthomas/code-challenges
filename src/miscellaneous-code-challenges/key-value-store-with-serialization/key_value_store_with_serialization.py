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

from typing import Any, Optional

DELIMINTER = ":"


def __get_data_type_from_value(value: Any) -> str:
    if isinstance(value, bool):
        return ["b", str(value)]
    if isinstance(value, float):
        return ["f", repr(value)]
    if isinstance(value, int):
        return ["i", str(value)]
    if isinstance(value, str):
        return ["s", str(value)]

    return ["n", ""]


def __get_value_from_data_and_type(value: str, data_type: str) -> Any:
    if data_type == "s":
        return value
    if data_type == "b":
        return value == "True"
    if data_type == "i":
        return int(value)
    if data_type == "f":
        return float(value)

    return None


def serialize(data: Optional[dict[str, Any]]) -> str:
    result = ""

    if not data:
        return result

    for key, value in data.items():
        _, key_final = __get_data_type_from_value(key)
        value_type, value_final = __get_data_type_from_value(value)
        key_len = len(key_final)
        value_len = len(value_final)

        result += f"{key_len}{DELIMINTER}{key_final}{value_len}{DELIMINTER}{value_type}{value_final}"

    return result


def deserialize(data: Optional[str]) -> dict[str, Any]:
    result = {}

    if not data:
        return result

    i = 0
    while i < len(data):
        key_len_s = ""
        while data[i] != DELIMINTER:
            key_len_s += data[i]
            i += 1

        key_len = int(key_len_s)
        i += 1

        key = data[i : i + key_len]
        i += key_len

        value_len_s = ""
        while data[i] != DELIMINTER:
            value_len_s += data[i]
            i += 1

        value_len = int(value_len_s)

        i += 1
        value_type = data[i]
        i += 1

        value = data[i : i + value_len]
        i += value_len

        result[key] = __get_value_from_data_and_type(value, value_type)

    return result


# data = {"na::me": "Nathan Thomas", "a,,,,ge": 38, "test\\_none": None, "float": 3.14}
# print(serialize(data))
# print(deserialize(serialize(data)))
