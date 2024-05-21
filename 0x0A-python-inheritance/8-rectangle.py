#!/usr/bin/python3

"""
Imported module: None
"""


class BaseGeometry:
    """An empty parent class

    Attributes:
    None

    """

    def area(self):
        """Raises an exception

        Args:
        None

        Returns:
        None

        """

        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """Validates @value is  an integer

        Args:
        name (str): name of the object
        value (str): integer value

        Returns:
        Void

        """

        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """A 2d shape with width and height

    Args:
    width (int): width of rectangle
    height (int): height of rectangle

    """

    def __init__(self, width, height):
        """Object constructor for class Rectangle

        Attributes:
        width (int): width of rectangle (Private)
        height (int): height of rectangle (Private)

        """

        BaseGeometry.integer_validator(width, int)
        BaseGeometry.integer_validator(height, int)
        self.__width = width
        self.__heigh1 = height
