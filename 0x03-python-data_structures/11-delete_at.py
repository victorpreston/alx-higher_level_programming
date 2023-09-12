#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """Delete items at a specific point in a list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
