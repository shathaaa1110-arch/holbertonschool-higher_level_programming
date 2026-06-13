#!/usr/bin/python3
"""
This module contains a function that prints a name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first_name> <last_name>'

    Args:
        first_name: First name (must be a string)
        last_name: Last name (must be a string, defaults to empty)

    Raises:
        TypeError: If first_name or last_name are not strings
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
