#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find biggest integer in a list"""
    if len(my_list) == 0:
        return (None)

    big = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > big:
            big = my_list[x]

    return (big)
