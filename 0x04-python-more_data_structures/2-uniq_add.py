#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    sum = 0
    for i in set(my_list):
        sum += i
    return sum
