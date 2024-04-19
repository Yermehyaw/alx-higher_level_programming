#!/usr/bin/python3

"""
Imported module: None
"""


def append_write(filename="", text=""):
    """Returns the no of chars added to a specified file

    Args:
    filename (str): name of file
    text (str): string to be added

    Returns:
    No of chars added

    """

    with open(filename, "a") as fopen:
        return fopen.write(text)
