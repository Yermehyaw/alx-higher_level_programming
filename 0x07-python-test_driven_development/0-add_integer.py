#!/usr/bin/python3

"""
Module Imported: None
"""


def add_integer(a, b=98):
    """Adds two integers

    Args:
    a (int): First no
    b (int): Second no

    Returns:
    Sum (int) of both integers

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
