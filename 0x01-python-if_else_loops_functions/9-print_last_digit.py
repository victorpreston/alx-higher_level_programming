#!/usr/bin/python3
def print_last_digit(number):
    """Print last digit of a number and return the digit"""
    print(abs(number) % 10, end="")
    return (abs(number) % 10)
