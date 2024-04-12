#!/usr/bin/python3

"""
Module Imported: None
"""


def say_my_name(first_name, last_name=""):
    """ Prints the Users name

    Attributes:
    first_name (str): Users first name
    last_name (str): Users last name

    Return (str):
    My name is <first name> <last name>
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name == "":
        print("My name is {}".format(first_name))
    else:
        print("My name is {} {}".format(first_name, last_name))
