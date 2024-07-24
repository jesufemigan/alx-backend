#!/usr/bin/env python3
"""
LIFO Caching
"""
from collections import OrderedDict

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    inherits from BaseCaching
    """
    def __init__(self):
        """
        initializes constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        puts item to cache
        """
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                first_key, _ = self.cache_data.popitem(True)
                print(f"DISCARD: {first_key}")
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        retrieves element
        """
        return self.cache_data.get(key)
