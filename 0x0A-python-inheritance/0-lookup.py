#!/usr/bin/python3

"""
Imported Module: None
"""


def lookup(obj):
    """Returns all attributes of an object as a list

    Args:
    obj (Unknown): obhect of any class

    Returns:
    A list of attrs

    """

    try:
        list_attr = list(dir(obj))
    except:
        raise TypeError("Invalid object passed")
    else:
        return (list_attr)
