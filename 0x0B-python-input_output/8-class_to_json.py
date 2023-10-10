#!/usr/bin/python3
"""Defining a Python function class_to_json"""


def class_to_json(obj):
    """Return the dictionary representation of a simple data structure."""
    return obj.__dict__
