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
        """Object initializer

        Args:
        width (int)
        height (int)
        x(int)
        y (int)
        id (int): identity no - automatically inherited from parent class

        """
        super().__init__(id)
        self.width(width)
        self.height(height)
        self.x(x)
        self.y(y)

    def width(self):
        """Returns width value
        """
        return self.__width

    def width(self, val):
        """Inits the value of width

        Args:
        val (int): value to be set

        """
        if isinstance(val, int):
            self.__width = val
        else:
            raise TypeError("Invalid number")

    def height(self):
        """Returns height value
        """
        return self.__height

    def height(self, val):
        """Inits the value of height

        Args:
        val (int): value to be set

        """
        if isinstance(val, int):
            self.__height = val
        else:
            raise TypeError("Invalid number")

    def x(self):
        """Returns x value
        """
        return self.__x

    def x(self, val):
        """Inits the value of x

        Args:
        val (int): value to be set

        """
        if isinstance(val, int):
            self.__x = val
        else:
            raise TypeError("Invalid number")

    def y(self):
        """Returns y  value
        """
        return self.__y

    def y(self, val):
        """Inits the value of y

        Args:
        val (int): value to be set

        """
        if isinstance(val, int):
            self.__y = val
        else:
            raise TypeError("Invalid number")
