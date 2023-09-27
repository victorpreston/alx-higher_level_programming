#!/usr/bin/python3
"""Definig class Square"""


class Square():
    """Defining class Square with valid prperties"""

    def __init__(self, size=0, position=(0, 0)):
        """"Initialize data for Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """"get size of Square"""
        return self.__size

    @property
    def position(self):
        """"get position of Square"""
        return self.__position

    @size.setter
    def size(self, value):
        """"Sets size of Square"""
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """"Sets position of Square"""
        if (type(value) is not tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (type(value[0]) is not int) or (type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif (value[0] < 0) or (value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """"get area of Square"""
        return self.size ** 2

    def my_print(self):
        """Prints the Square"""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print("")
            for i in range(self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
