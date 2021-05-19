#!/usr/bin/python3
"""Square with size"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2
