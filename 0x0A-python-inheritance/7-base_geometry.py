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
            raise TypeError("name must be  a string")
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
