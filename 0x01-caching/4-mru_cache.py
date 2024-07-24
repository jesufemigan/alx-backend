#!/usr/bin/env python3
"""
MRU cahcing
"""
from collections import OrderedDict


BaseCaching = __import__("base_caching").BaseCaching()


class MRUCaching(BaseCaching):
    """
    inherits from base class
    """
