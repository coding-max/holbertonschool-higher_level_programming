#!/usr/bin/python3
"""Compare 2 squares"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0):
        """Instantiation with optional size"""
        self.size = size

    @property
    def size(self):
        """Property to retrieve size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Property setter to set size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Method to compare using == operator"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Method to compare using != operator"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Method to compare using > operator"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Method to compare using >= operator"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Method to compare using < operator"""
        return self.area() < other.area()

    def __le__(self, other):
        """Method to compare using <= operator"""
        return self.area() <= other.area()
