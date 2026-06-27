#!/usr/bin/python3
"""
This module defines a base class BaseGeometry.
"""


class BaseGeometry:
    """
    A class that represents basic geometry operations.
    """

    def area(self):
        """
        Raises an Exception indicating area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates if a value is an integer strictly greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
