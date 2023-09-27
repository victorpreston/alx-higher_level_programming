#!/usr/bin/python3
"""Defining a class Square"""


class Square:
    """Defining a class Squate"""
    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): Size of new Square.
        """
        self.__size = size

    @property
    def size(self):
        """Function retrieves a Square"""
        return(self.__size)

    @size.setter
    def size(self, value):
        """Set properties of new Square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of Square"""
        return(self.__size * self.__size)

    def my_print(self):
        """Prints output in stdout"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
