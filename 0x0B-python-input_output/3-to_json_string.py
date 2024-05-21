#!/usr/bin/python3

"""Imported module: json

consists several methods for serializing and deserializing python data objects
like ints, dicts, bools etc

"""
import json


def to_json_string(my_obj):
    """Returns the json rep of a python data object

    Args:
    my_obj (unknown): an object

    Returns:
    json string

    """

    return json.dumps(my_obj)
