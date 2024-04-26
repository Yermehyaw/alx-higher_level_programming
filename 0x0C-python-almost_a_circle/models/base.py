#!/usr/bin/python3

"""
Imported module(s): None
"""


class Base:
    """Base clasd for all incoming subclasses. A 2d shape

    Attributes:
    __nb_objects(int): no pf obects made from tgis class

    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Object constructor/initializer

        Arguments:
        id (int): id no of the object

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returms the JSON string representation of a list of dictionaries

        Args:
        list_dictionaries (list): A lost of dictionaries

        """
        if list_dictionaries is None:
            return "[]"
        elif not isinstance(list_dictionaries, list):
            raise TypeError("Argument must be a list")
        else:
            json_str = json.dumps(list_dictionaries)
            return json_str
