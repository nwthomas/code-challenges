"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

Example 1:
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4

Constraints:
1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.head = None
        self.tail = None
        self.cache = {}

    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        if self.length == 1:
            return self.cache[key].value
        
        moving_node = self.cache[key]
        prev_node = moving_node.prev
        next_node = moving_node.next
        
        if prev_node:
            prev_node.next = next_node
        else:
            return moving_node.value
            
        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node
            
        self.head.prev = moving_node
        moving_node.next = self.head
        moving_node.prev = None
        self.head = moving_node
        
        return self.head.value
        

    def put(self, key: int, value: int) -> None:
        if not self.head:
            self.length += 1
            self.head = Node(value, key)
            self.tail = self.head
            self.cache[key] = self.head
        elif key in self.cache:
            self.get(key)
            self.head.value = value
        else:     
            self.length += 1
            new_node = Node(value, key, self.head)
            self.head.prev = new_node
            self.head = new_node
            self.cache[key] = new_node
            
            if self.length > self.capacity:
                deleted_node = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                del self.cache[deleted_node.key]
                self.length -= 1
        
class Node:
    def __init__(self, value, key, next_node = None, prev_node = None):
        self.value = value
        self.key = key
        self.next = next_node
        self.prev = prev_node