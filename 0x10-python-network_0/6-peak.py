#!/usr/bin/python3
"""script for finding peak in list of ints, interview prep
"""

"""
    THOUGHT PROCESS
        it is not sorted, so sorting would take n(log(n))
            -> not worth sorting
        looping through and keeping track of max (brute force)
            -> O(n)

        possibly looping from each end reducing to 1/2 run time
            -> still O(n)
"""


def find_peak(list_of_integers):
    """Improved implementation for question"""
    if not list_of_integers:
        return None

    max_i = 0
    for i in range(1, len(list_of_integers)):
        if list_of_integers[i] > list_of_integers[max_i]:
            max_i = i
        elif list_of_integers[i] < list_of_integers[max_i]:
            break

    return list_of_integers[max_i]
