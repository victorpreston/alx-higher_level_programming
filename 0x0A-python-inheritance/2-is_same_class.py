#!/usr/bin/python3
"""Defining a class is_same_class"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        return True or False
    """
    if type(obj) == a_class:
        return True
    return False
