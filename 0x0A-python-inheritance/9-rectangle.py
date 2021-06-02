#!/usr/bin/python3
"""Full rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """representation of a rectangle"""

    def __init__(self, width, height):
        """instantiation of the rectangle"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """custom str method for print the rectangle"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)

    def area(self):
        """computes the area of the retangle"""
        return self.__width * self.__height
