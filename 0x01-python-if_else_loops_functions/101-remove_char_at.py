#!/usr/bin/python3
def remove_char_at(str, n):
    """Creating copies of a string"""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])
