#!/usr/bin/python3

"""
Imported module(s):

json
intercoverts python objects into transferrable strings or json objects

rectangle
A module containig attributes that define a 2d square
"""
import json
# from models.rectangle  import Rectangle  # circular import


class Base:
    """Base clasd for all incoming subclasses. A 2d shape

    Attributes:
    __nb_objects(int): no pf obects made from tgis class

    """
    __nb_objects = 0
    """int: no of objects made from this class
    """

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
        list_dictionaries (list): A list of dictionaries

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
        with open(str(cls.__class__) + ".json", "w") as f:
            if list_objs is None or not isinstance(list_objs, list):
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
            obj = json.loads(json_string)
            return obj

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

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance of the base method with all its attributes set

        Args:
        dictionary (dict): keyworded variable no of argumemts

        """
        obj = cls.Rectangle(10, 10)
        obj.update(None, **dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a json file

        Args:
        None

        """
        with open(str(cls.__class__) + ".json", "r") as f:
            list_dict = json.load(f)
            # convert a list of dictionaries(like a list of **kwargs) to a list
            list_instances = []
            for dictionary in list_dict:
                list_instances.append(cls.create(dictionary))
            return list_instances
