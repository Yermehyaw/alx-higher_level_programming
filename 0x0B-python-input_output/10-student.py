#!/usr/bin/python3

"""Imported module: None
"""


class Student:
    """An individual who attends a school

    Attributes:
    first_name: students first name
    last_name: students last name
    age: students age

    """
    def __init__(self, first_name, last_name, age):
        """Class constructor

        Arguments:
         first_name: students first name
        last_name: students last name
        age: students age

        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict of specified class attributes

        Args:
        attrs (list): list of attributes to be retrieved (list of strings)

        Returns:
        A dict

        """

        if attrs is None:
            return {'first_name': self.first_name, 'last_name': self.last_name,
                    'age': self.age}
        not_founds = []
        for attr in attrs:
            try:
                getattr(self, attr)
            except AttributeError:  # attribute not found
                not_founds.append(attr)  # store all not found attr in a list
        # get ONLY attrs of the object which is not in the not_founds list
        return {attr: getattr(self, attr) for attr in attrs
                if not attr.startswith('__') and attr not in not_founds}
