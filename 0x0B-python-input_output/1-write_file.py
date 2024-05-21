#!/usr/bin/python3

"""
Imported module: None
"""


def write_file(filename="", text=""):
    """Returns the no of chars written to a specified file

    Args:
    filename (str): name of file
    text (str): string to be written

    Returns:
    No of chars written

    """

    with open(filename, "w") as fopen:
        return fopen.write(text)
