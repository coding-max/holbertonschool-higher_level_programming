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

    @property
    def position(self):
        """Property to retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        """Property setter to set position"""
        if ((type(value) != tuple) or (len(value) != 2) or
                not all((type(number) != int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with char #"""
        for i in range(self.__size):
            for j in  range(self.__size):
                print("#", end="")
            print("")
        if self.__size == 0:
            print("")
