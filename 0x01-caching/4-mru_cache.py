#!/usr/bin/env python3
"""
MRU cahcing
"""
from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching


class MRUCache(BaseCaching):
    """
    inherits from base class
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        put into cache
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print(f"DISCARD: {mru_key}")
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        retrieves item
        """
        if  key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
