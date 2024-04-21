#!/usr/bin/python3

"""Imported module: None
"""


def class_to_json(obj):
    """Returns a dict of attributes of a userdefined class

    Args:
    obj (unknown): an object

    Returns:
    A dict

    """

    attr_list = dir(obj)
    dict_json = {attr: getattr(obj, attr) for attr in attr_list if not
                 attr.startswith('__')}
    return dict_json
