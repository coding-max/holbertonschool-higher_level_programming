#!/usr/bin/python3
"""Square with size"""


class Square:
    """Representation of a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and optional position"""
        self.size = size
        self.position = position

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
                (type(value[0]) != int) or (value[0] < 0) or
                (type(value[1]) != int) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """Public instance method that prints the square with char #"""
        if self.__size == 0:
            print("")
            return
        "Not empty (size != 0)"
        for new_line in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            print("")

    def __str__(self):
        """Custom __str__ method to print a square"""
        for new_line in range(self.__position[1]):
            print("")
        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            if (row != self.__size - 1):
                print("")
        return ("")
