#!/usr/bin/python3
"""Only sub class of"""


def is_kind_of_class(obj, a_class):
    """checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class"""

    if issubclass(type(obj), a_class) and not isinstance(obj, a_class):
        return True
    return False
