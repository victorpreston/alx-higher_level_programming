#!/usr/bin/python3
"""Defining a class MyList."""


class MyList(list):
    """Implementing sorted printing"""

    def print_sorted(self):
        """Print a sorted list"""
        print(sorted(self))
