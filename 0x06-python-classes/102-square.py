#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Representing  Square"""

    def __init__(self, size=0):
        """Initializing new Square.

        Args:
            size (int): Size of new Square.
        """
        self.size = size

    @property
    def size(self):
        """get & set size of Square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returning current area of Square"""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Defining the == comparision to a Square"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Defining the != comparison to Square"""
        return self.area() != other.area()

    def __lt__(self, other):
        """Defining the < comparison to Square"""
        return self.area() < other.area()

    def __le__(self, other):
        """Defining the <= comparison to Square"""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Defining the > comparison to Square"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Defining the >= compmarison to Square"""
        return self.area() >= other.area()
