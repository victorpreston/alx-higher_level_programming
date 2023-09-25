#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the result of the ivision a/b"""
    try:
        d = a / b
    except (TypeError, ZeroDivisionError):
        d = None
    finally:
        print("Inside result: {}".format(d))
    return (d)
