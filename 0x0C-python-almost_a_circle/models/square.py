#!/usr/bin/python3

"""
Imported module: base

Base module describing the basic properties of a 2d shape
"""
from models.base import Base


class Square(Rectangle):
    """A 2d shape with length and breadth

    Attributes:
    size (int)
    __x (int): x-coordinates
    __y (int): -coordinates
    id (int)

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Object initializer

        Args:
        size (int)
        x(int)
        y (int)
        id (int): identity no - automatically inherited from parent class

        """
        super().__init__(id, weight, height, x, y)
        self.size = size  # property setter is automatically called

    @property
    def size(self):
        """Returns width value
        """
        return self.size

    @size.setter
    def size(self, size):
        """Inits the value of width

        Args:
        size (int): value to be set

        """
        if not isinstance(size, int):
            raise TypeError("size must be a integer")
        elif size <= 0:
            raise ValueError("size must be > 0")
        else:
            self.width = size
            self.height = size

    # Define a __str__ method
    def __str__(self):
        """Handle how output is given to stdout for this class

        Args:
        None

        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - \
        {self.size}"

    # Update the attributes of the shape
    def update(self, *args, **kwargs):
        """Update the class Rectangle attributes

        Args:
        args (tuple): positional variable number of integers
        kwargs (dict): keyworded variable number of integers

        """
        if args is None:
            if kwargs is None:
                raise TypeError("Enter a valid number of arguments")
            else:  # kwargs in not None
                for key, value in kwargs.items():
                    match str(key):
                        case "id":
                            self.id = value
                        case "size":
                            self.size = value
                        case "x":
                            self.x = value
                        case "y":
                            self.y = value
        else:
            i = 0
            while i < len(args):
                self.size = args[i]
                i += 1
                self.height = args[i]
                i += 1
                self.x = args[i]
                i += 1
                self.y = args[i]
                i += 1
                self.id = args[i]
                i += 1

    def to_dictionary(self):
        """Returns the dict representation of the class

        Args:
        None

        """
        # Returns a dict from a list of tuples
        return dict([('id', self.id), ('size', self.size),
                     ('x', self.x), ('y', self.y)])
