#!/usr/bin/python3

"""Imported module: json

consists several methods for serializing and deserializing python data objects
like ints, dicts, bools etc

"""
import json


def from_json_string(my_str):
    """Returns the python data object of a json rep

    Args:7
    my_obj (unknown): an object

    Returns:
    python data object

    """

    return json.load(my_str)
