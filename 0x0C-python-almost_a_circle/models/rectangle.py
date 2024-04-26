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
        self.__width = width  # property setter is automatically called
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Returns width value
        """
        return self.__width

    @width.setter
    def width(self, val):
        """Inits the value of width

        Args:
        val (int): value to be set

        """
        if not isinstance(val, int):
            raise TypeError("width must be a integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """Returns height value
        """
        return self.__height

    @height.setter
    def height(self, val):
        """Inits the value of height

        Args:
        val (int): value to be set

        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """Returns x value
        """
        return self.__x

    @x.setter
    def x(self, val):
        """Inits the value of x

        Args:
        val (int): value to be set

        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """Returns y  value
        """
        return self.__y

    @y.setter
    def y(self, val):
        """Inits the value of y

        Args:
        val (int): value to be set

        """
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    # Return Area
    def area(self):
        """Returns the area of the shape

        Args:
        None

        """
        return self.width * self.length

    # Display the Shape
    def display(self):
        """Prints the shape to stdout using "#"

        Args:
        None

        """
        print("\n" * self.y)
        for i in range(self.length):
            print(" " * self.x)
            for j in range(self.width):
                print("#", end="")
            print("")

    # Define a __str__ method
    def __str__(self):
        """Handle how output is given to stdout for this class

        Args:
        None

        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
        - {self.width}/{self.height}"

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
                            self.id = id
                        case "width":
                            self.width = value
                        case "height":
                            self.height = value
                        case "x":
                            self.x = value
                        case "y":
                            self.y = value
        else:
            i = 0
            while i < len(args):
                self.id = args[i]
                i += 1
                self.width = args[i]
                i += 1
                self.height = args[i]
                i += 1
                self.x = args[i]
                i += 1
                self.y = args[i]
                i += 1
