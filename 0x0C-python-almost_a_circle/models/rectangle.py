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
    id (int): identity no of obj derived/instantiated from this class

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Object initializer

        Args:
        width (int)
        height (int)
        3x (int): positive x coordinate
        y (int): positive y coordinate
        id (int): identity no - automatically inherited from parent class

        """
        super().__init__(id)
        self.__width = width  # property setter is automatically called
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Getter: Returns width value
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Setter: Edits width value
        """
        if not isinstance(val, int):
            raise TypeError("width must be a integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """Getter: Returns height value
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Setter: Edits height value
        """
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        """Getter: Returns x value
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Setter: Edits x value
        """
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """Getter: Returns y  value
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Setter: Edits y value
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

        Returns:
            area of object

        """
        return self.width * self.height

    # Display the Shape
    def display(self):
        """Prints the shape to stdout using "#"

        Args:
           None

        Returns:
           None

        """
        print("\n" * self.y)
        for i in range(self.height):
            print(" " * self.x)
            for j in range(self.width):
                print("#", end="")
            print("")

    # Define a __str__ method
    def __str__(self):
        """Handle how output is given to stdout for this class

        Args:
           None

        Returns:
           string rep of the class

        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y}\
        - {self.width}/{self.height}"

    # Update the attributes of the shape
    def update(self, *args, **kwargs):
        """Update the class Rectangle attributes

        Args:
           args (tuple): positional variable number of integers
           kwargs (dict): keyworded variable number of integers

        Returns:
           None

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

    def to_dictionary(self):
        """Returns the dict representation of the class

        Args:
           None

        Returns:
           A dict

        """
        # Returns a dict from a list of tuples
        return dict([('id', self.id), ('width', self.width),
                     ('height', self.height), ('x', self.x), ('y', self.y)])
