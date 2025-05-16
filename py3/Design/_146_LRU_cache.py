"""
Design a data structure that follows the constraints of a
**[Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU)**.

Implement the `LRUCache` class:

- `LRUCache(int capacity)` Initialize the LRU cache with **positive** size `capacity`.
- `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
- `void put(int key, int value)` Update the value of the `key` if the `key` exists. Otherwise, add the `key-value` pair
to the cache. If the number of keys exceeds the `capacity` from this operation, **evict** the least recently used key.

The functions `get` and `put` must each run in `O(1)` average time complexity.
"""

class Node(object):
    def __init__(self, node_key, val):
        self.node_key = node_key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.head = Node('head', 'head')
        self.tail = Node('tail', 'tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_size = capacity
        self.curr_size = 0
        self.node_lookup = {}

    @staticmethod
    def remove_node(node):
        node_after = node.next
        node_before = node.prev
        node_before.next = node_after
        node_after.prev = node_before

    def move_to_end(self, node):
        prev_node_tail = self.tail.prev
        prev_node_tail.next = node
        node.prev = prev_node_tail
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.node_lookup:
            return -1
        node = self.node_lookup[key]
        node_val = node.val
        self.remove_node(node)
        self.move_to_end(node)
        return node_val

    def put(self, key: int, value: int) -> None:
        if key in self.node_lookup:
            node = self.node_lookup[key]
            node.val = value
            self.remove_node(node)
            self.move_to_end(node)
        else:
            if self.curr_size >= self.max_size:
                lru_node = self.head.next
                del self.node_lookup[lru_node.node_key]
                self.remove_node(lru_node)
                self.curr_size -= 1

            new_node = Node(key, value)
            self.node_lookup[key] = new_node
            self.move_to_end(new_node)
            self.curr_size += 1


if __name__ == '__main__':
    # begin
    s = LRUCache(100)
    s.put(1,1)
    s.put(1, 1)
    s.put(2, 2)
    s.get(1)
    s.put(3, 3)
    s.get(2)
    s.put(4, 4)
    s.get(1)
    s.get(3)
    s.get(4)




