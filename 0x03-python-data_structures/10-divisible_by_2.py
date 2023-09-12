#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Finds all multiples of 2 in the list"""
    multiples = []
    for x in range(len(my_list)):
        if my_list[x] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return multiples
