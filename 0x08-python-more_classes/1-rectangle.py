#!/usr/bin/python3
"""1 - Real definition of a rectangle"""


class Rectangle():
    """Representation of a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation with width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Property setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Property setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
