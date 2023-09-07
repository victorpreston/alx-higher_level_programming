#!/usr/bin/python3

def magic_calculation(a, b):
    """Match bytecode provided"""
    add, sub = lambda a, b: a + b, lambda a, b: a - b

    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(a, b))
