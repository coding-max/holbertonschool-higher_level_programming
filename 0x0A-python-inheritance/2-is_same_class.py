#!/usr/bin/python3
"""Exact same object"""


def is_same_class(obj, a_class):
    """checks if an object is exactly an instance of a given class"""

    if isinstance(obj, a_class):
        return True
    return False
