#!/usr/bin/python3
"""
Module: 6-print_sorted_dictionary
Prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary: A dictionary with string keys

    Prints:
        The dictionary items sorted by keys alphabetically.
        Only sorts keys of the first level (doesn't sort nested dicts).

    Example:
        >>> a_dictionary = {'language': "C", 'Number': 89}
        >>> print_sorted_dictionary(a_dictionary)
        Number: 89
        language: C
    """
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
