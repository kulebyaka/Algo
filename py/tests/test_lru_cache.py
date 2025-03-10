import pytest
from py._146_LRU_cache import LRUCache

class TestLRUCache:
    def test_lru_cache_basic_operations(self):
        # Test basic operations
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)  # This should evict key 2
        assert cache.get(2) == -1
        cache.put(4, 4)  # This should evict key 1
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_lru_cache_update_existing(self):
        # Test updating existing values
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(1, 10)  # Update value and make it most recently used
        cache.put(3, 3)   # This should evict key 2 since 1 was recently used
        assert cache.get(2) == -1
        assert cache.get(1) == 10

    def test_lru_cache_capacity_one(self):
        # Test with capacity of 1
        cache = LRUCache(1)
        cache.put(1, 1)
        assert cache.get(1) == 1
        cache.put(2, 2)
        assert cache.get(1) == -1
        assert cache.get(2) == 2

    def test_lru_cache_get_updates_order(self):
        # Test that get updates LRU order
        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1  # Makes 1 most recently used
        cache.put(3, 3)  # Should evict 2
        assert cache.get(2) == -1
        assert cache.get(1) == 1
        assert cache.get(3) == 3
