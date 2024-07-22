#!/usr/bin/env python3
'''
simple helper function
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    return a tuple of size two containing a start index and an end index
    '''
    end_index = page * page_size
    return (end_index - page_size, end_index)
