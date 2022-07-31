from lru_cache import LRUCache
import unittest

class TestLRUCache(unittest.TestCase):
    def test_instantiates_new_lru_cache(self):
        """Instantiates a new LRU Cache"""
        lru = LRUCache(4)
        self.assertIsInstance(lru, LRUCache)
        self.assertEqual(lru.capacity, 4)
        self.assertEqual(lru.length, 0)
        self.assertIsNone(lru.head)
        self.assertIsNone(lru.tail)
        self.assertEqual(lru.cache, {})

    def test_removes_old_cached_values(self):
        """Does not contain old nodes if removed from cache"""
        lru = LRUCache(2)
        lru.put("3", 3)
        lru.put("2", 2)
        lru.get("3")
        lru.put("1", 1)
        self.assertEqual(lru.length, 2)
        self.assertEqual(lru.head.value, 1)
        self.assertEqual(lru.tail.value, 3)
        self.assertEqual(lru.get("2"), -1)

    def test_moves_accessed_values_to_head(self):
        """Moves current values to head of cache if accessed"""
        lru = LRUCache(10)
        lru.put("1", 1)
        lru.put("2", 2)
        lru.put("3", 3)
        lru.put("4", 4)
        
        self.assertEqual(lru.head.value, 4)
        self.assertEqual(lru.tail.value, 1)

        lru.get("1")

        self.assertEqual(lru.head.value, 1)
        self.assertEqual(lru.tail.value, 2)

    def test_get_returns_value(self):
        """The get method returns the accessed value"""
        lru = LRUCache(10)
        lru.put("test", "value")

        self.assertEqual(lru.get("test"), "value")

if __name__ == "__main__":
    unittest.main()