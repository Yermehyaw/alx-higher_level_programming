#!/usr/bin/python3

"""
Imporred Module: None
"""


def inherits_from(obj, a_class):
    """Returns a bool if an object is a direct or ibdirect inheritance of
    a class

    Args:
    obj (unknown): Object name
    a_class (unknown): ckass name

    Returns:
    True or False

    """

    if issubclass(type(obj), type(a_class)) or isinstance(type(obj), a_class):
        return True
    else:
        return False
