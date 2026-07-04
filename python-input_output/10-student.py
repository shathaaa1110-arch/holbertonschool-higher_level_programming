#!/usr/bin/python3
"""Module that defines a Student class."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        If attrs is a list of strings, return only those attributes.
        Otherwise, return all attributes.
        """
        if isinstance(attrs, list):
            new_dict = {}
            for key in attrs:
                if key in self.__dict__:
                    new_dict[key] = self.__dict__[key]
            return new_dict

        return self.__dict__
