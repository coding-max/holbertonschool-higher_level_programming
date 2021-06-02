#!/usr/bin/python3
"""Square #1"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """representation of a square"""

    def __init__(self, size):
        """instantiation of the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
