#!/usr/bin/python3

"""Imported module: json

consists several methods for serializing and deserializing python data objects
like ints, dicts, bools etc

"""
import json


def load_from_json_file(filename):
    """Creates an object from a json file

    Args:
    filename (str): name of file

    Returns:
    A python data object

    """

    with open(filename) as fread:
        for line in fread:
            json_obj = json.loads(line)  # json_obj: obj made frm json
            return json_obj
