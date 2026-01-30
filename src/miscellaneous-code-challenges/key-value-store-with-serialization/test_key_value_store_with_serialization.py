from key_value_store_with_serialization import serialize, deserialize


def test_serialize():
    result = serialize({"key": "val,u:e", "another,:/|key": "valvalval$%&*^%n"})
    assert result == "3:key:7:val,u:e:14:another,:/|key:16:valvalval$%&*^%n"


def test_deserialize():
    result = deserialize("3:key:7:val,u:e:14:another,:/|key:16:valvalval$%&*^%n")
    assert result == {"key": "val,u:e", "another,:/|key": "valvalval$%&*^%n"}
