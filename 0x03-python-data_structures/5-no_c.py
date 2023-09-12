#!/usr/bin/python3
def no_c(my_string):
    """Removes all c and C characters from a string"""
    new_string = ""
    for j in range(len(my_string)):
        if my_string[j] != 'c' and my_string[j] != 'C':
            new_string += my_string[j]
    return new_string
