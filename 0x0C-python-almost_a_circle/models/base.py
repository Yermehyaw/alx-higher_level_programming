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
            __nb_objects += 1
            self.id = __nb_objects
