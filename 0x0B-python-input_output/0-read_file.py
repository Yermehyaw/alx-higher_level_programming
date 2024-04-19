#!/usr/bin/python3

"""
Imported module: None
"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
    filename (str): name of file

    Returns:
    None

    """

    with open(filename) as fopen:
        fread = fopen.read()
        print(fread)
