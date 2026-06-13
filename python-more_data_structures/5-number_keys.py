#!/usr/bin/python3
"""
Module: 5-number_keys
Returns the number of keys in a dictionary.
"""


def number_keys(a_dictionary):
    """
    Returns the number of keys in a dictionary.

    Args:
        a_dictionary: A dictionary

    Returns:
        The number of keys in the dictionary.

    Example:
        >>> a_dictionary = {'language': "C", 'number': 13}
        >>> nb_keys = number_keys(a_dictionary)
        >>> print("Number of keys: {:d}".format(nb_keys))
        Number of keys: 2
    """
    return len(a_dictionary)
