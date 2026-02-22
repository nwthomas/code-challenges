from key_value_store_with_serialization import serialize, deserialize


def test_serialize():
    result = serialize(
        {
            "key": "val,u:e",
            "another,:/|key": "valvalval$%&*^%n",
            "float": 4.21,
            "none": None,
            "bool": False,
        }
    )
    assert (
        result
        == "3:key7:sval,u:e14:another,:/|key16:svalvalval$%&*^%n5:float4:f4.214:none0:n4:bool5:bFalse"
    )


def test_deserialize():
    result = deserialize(
        "3:key7:sval,u:e14:another,:/|key16:svalvalval$%&*^%n5:float4:f4.214:none0:n4:bool5:bFalse"
    )
    assert result == {
        "key": "val,u:e",
        "another,:/|key": "valvalval$%&*^%n",
        "float": 4.21,
        "none": None,
        "bool": False,
    }
