#!/usr/bin/python3
"""
Modules Imported: None
"""


def find_peak(list_of_integers):
    """
    Finds the max integr in the list

    Attributes:
    list_of_integers: A list of positive/negative numbers (list)

    Return:
    Peak integer
    """
    if not isinstance(list_of_integers, list):
        return None
    list_len = len(list_of_integers)
    if list_len == 0:
        return None
    list_of_integers.sort()
    return list_of_integers[list_len - 1]
