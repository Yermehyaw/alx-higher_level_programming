#!/usr/bin/python3

"""Imported module: json

consists several methods for serializing and deserializing python data objects
like ints, dicts, bools etc

"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj json rep into a specified file

    Args:7
    my_obj (unknown): an objec
    filename (str): name of file

    Returns:
    No of chars written

    """

    with open(filename, "w") as fread:
        json_rep = json.dumps(my_obj)
        return fread.write(json_rep)
