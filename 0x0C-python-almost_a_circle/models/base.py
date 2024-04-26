#!/usr/bin/python3

"""
Imported module(s):

json
intercoverts python objects into transferrable strings or json objects
"""
import json


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a json string rep into a file

        Args:
        list_objs (list): List of python data objects

        """
        if not isinstance(list_objs, list):
            raise TypeError("Argument must be a list")
        for obj in list_objs:
            if not isinstance(obj, Base):
                raise TypeError("Object is not of class Base")
        with open(list_objs[0].__class__ + ".json", "w") as f:
            if list_objs is None:
                f.close()
            else:
                f = to_json_string(list_objs)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dictionaries from a json string representation

        Args:
        json_string (str): a json string rep of a list

        """
        if json_string is None or json_string == "":
            return list()
        else:
            obj = json.dumps(json_string)
            return obj
