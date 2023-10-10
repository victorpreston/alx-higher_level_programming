#!/usr/bin/python3
"""Defining a function read_file"""


def read_file(filename=""):
    """Print the contents of a UTF8."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
