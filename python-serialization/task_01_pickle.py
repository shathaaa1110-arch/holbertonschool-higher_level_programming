#!/usr/bin/env python3
"""Module for serializing and deserializing custom objects."""

import pickle


class CustomObject:
    """Represent a custom object."""

    def __init__(self, name, age, is_student):
        """Initialize the object."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to a file."""
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, pickle.PickleError, EOFError):
            return None
