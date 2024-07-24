#!/usr/bin/env python3
"""
FIFO caching
"""
from collections import OrderedDict
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from base class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        puts data into cache
        """
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, _ = self.cache_data.popitem(False)
            print(f"DISCARD: {first_key}")
            return

    def get(self, key):
        """
        retrieves data from cache
        """
        self.cache_data.get(key)
