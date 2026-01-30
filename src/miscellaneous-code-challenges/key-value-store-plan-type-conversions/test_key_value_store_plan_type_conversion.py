from key_value_store_plan_type_conversions import KeyValueStoreWithTimestamps


def test_key_value_store_plan_type_conversions():
    store = KeyValueStoreWithTimestamps()
    store.set_at("key", "val", 20)
    store.set_at("key", "val1", 20)
    store.set_at("key", "val3", 10)
    store.set_at("key", "val10", 15)
    assert store.store == {
        "key": [
            {"value": "val3", "timestamp": 10},
            {"value": "val10", "timestamp": 15},
            {"value": "val", "timestamp": 20},
            {"value": "val1", "timestamp": 20},
        ]
    }
    assert store.get_at("key", 20) == "val1"
    assert store.get_at("key", 16) == "val10"
    store.set_at("key", "valthreeve", 16)
    assert store.store == {
        "key": [
            {"value": "val3", "timestamp": 10},
            {"value": "val10", "timestamp": 15},
            {"value": "valthreeve", "timestamp": 16},
            {"value": "val", "timestamp": 20},
            {"value": "val1", "timestamp": 20},
        ]
    }
    assert store.get_at("key", 16) == "valthreeve"
