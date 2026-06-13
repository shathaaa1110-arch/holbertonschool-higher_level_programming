#!/usr/bin/python3
"""
Module: 7-update_dictionary
Replaces or adds key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.
    
    Args:
        a_dictionary: A dictionary
        key: The key to add or update (always a string)
        value: The value to set (any type)
    
    Returns:
        The updated dictionary.
        If the key exists, its value is replaced.
        If the key doesn't exist, it is created with the new value.
    
    Example:
        >>> a_dictionary = {'language': "C", 'number': 89, 'track': "Low level"}
        >>> new_dict = update_dictionary(a_dictionary, 'language', "Python")
        >>> print(new_dict)
        {'language': 'Python', 'number': 89, 'track': 'Low level'}
        
        >>> new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
        >>> print(new_dict)
        {'language': 'Python', 'number': 89, 'track': 'Low level', 'city': 'San Francisco'}
    """
    a_dictionary[key] = value
    return a_dictionary
