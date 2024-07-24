#!/usr/bin/env python3
"""
basic dictionary
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    a class that inherits from the parent class
    and is a caching system
    """
    def __init__(self):
        """
        initial constructor
        """
        super().__init__()

    def put(self, key, item):
        """
        method to put item in cache
        """
        self.cache_data[f'{key}'] = item

    def get(self, key):
        """
        get value from cache
        """
        return self.cache_data.get(f'{key}')
