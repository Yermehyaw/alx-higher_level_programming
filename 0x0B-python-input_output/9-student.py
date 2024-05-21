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

    def to_json(self):
        """Returns a dict of this class's attributes

        Returns:
        A dict

        """

        return {'first_name': self.first_name, 'last_name': self.last_name,
                'age': self.age}
