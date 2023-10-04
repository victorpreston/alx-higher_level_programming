#!/usr/bin/python3
"""Defining an addition function"""


def add_integer(a, b=98):
    """ adding integers
        Arguments:
        @a: First Integer.
        @b: Second Integer.
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
