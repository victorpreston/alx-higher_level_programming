#!/usr/bin/python3
"""
Defining a class LockedClass

"""


class LockedClass():
    """Class preventing creation of dynamic attributes"""
    __slots__ = ['first_name']

    def __init__(self):
        """Init program method"""
        pass
