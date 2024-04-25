#!/usr/bin/python3

"""
Imported module: base

Base module describing the basic properties of a 2d shape
"""
from models.base import Base


class Rectangle(Base):
    """A 2d shape with length and breadth

    Attributes:
    __width (int)
    __height (int)
    __x (int): x-coordinates
    __y (int): -coordinates

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.set_width(width)
        self.set_height(height)
        self.set_x(x)
        self.set_y(y)
        super().__init__(id)

    def get_width(self):
        return self.__width

    def set_width(self, val):
        if isinstance(val, int):
            self.__width = val
        else:
            raise TypeError("Invalid number")

    def get_height(self):
        return self.__height

    def set_height(self, val):
        if isinstance(val, int):
            self.__height = val
        else:
            raise TypeError("Invalid number")

    def get_x(self):
        return self.__x

    def set_x(self, val):
        if isinstance(val, int):
            self.__x = val
        else:
            raise TypeError("Invalid number")

    def get_y(self):
        return self.__y

    def set_y(self, val):
        if isinstance(val, int):
            self.__y = val
        else:
            raise TypeError("Invalid number")
