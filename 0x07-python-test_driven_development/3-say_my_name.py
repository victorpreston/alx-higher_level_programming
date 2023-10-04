#!/usr/bin/python3
"""Defining a function say_my_name"""


def say_my_name(first_name, last_name=""):
    """Printing first & last name.
        Arguments:
            @first_name: First name to be printed.
            @second_name: Last name to be printed.
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
