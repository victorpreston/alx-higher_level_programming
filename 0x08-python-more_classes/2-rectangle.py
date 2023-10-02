#!/usr/bin/python3
"""Defining a class Rectangle"""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle.

        Args:
            width (int): Width of Rectangle.
            height (int): Height of Rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get & set width property"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get & set height property"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of Rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Perimeter of Rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
