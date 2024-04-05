#!/usr/bin/python3

"""
Modiule Imported: None
"""


class Square():
    """A 2d shape with four equal sides

    Attributes:
    __size (int): Length of the square

    """

    def __init__(self, size=0):
        """Square class initialization variables

        Args:
        size (int): User defined length of Sqare instance

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        def area(self):
            """Returns the area of a class Square object

            Args:
            None

            """

            return (self.__size * self.__size)
