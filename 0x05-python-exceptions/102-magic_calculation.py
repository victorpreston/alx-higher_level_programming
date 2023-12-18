#!/usr/bin/python3

def magic_calculation(a, b):
    p = 0
    for x in range(1, 3):
        try:
            if x > a:
                raise Exception('Too far')
            else:
                p += a ** b / x
        except Exception:
            p = b + a
            break
    return (p)
