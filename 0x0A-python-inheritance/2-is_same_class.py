#!/usr/bin/python3

"""
Imported Module: None
"""


def is_same_class(obj, a_class):
    """ Returns a bool if an obhect is exactly tge sane with a specified class

    Args:
    obj (Unknown): Object name
    a_class (Unknown): class name

    Returns:
    True or False

    """

    if type(obj) == a_class:
        return True
    else:
        return False
