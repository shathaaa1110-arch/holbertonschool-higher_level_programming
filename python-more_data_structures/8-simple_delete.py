#!/usr/bin/python3
"""
Module: 8-simple_delete
Deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.
    
    Args:
        a_dictionary: A dictionary
        key: The key to delete (always a string, default is empty string)
    
    Returns:
        The updated dictionary.
        If the key doesn't exist, the dictionary won't change.
    
    Example:
        >>> a_dictionary = {'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3]}
        >>> new_dict = simple_delete(a_dictionary, 'track')
        >>> print(new_dict)
        {'language': 'C', 'Number': 89, 'ids': [1, 2, 3]}
        
        >>> new_dict = simple_delete(a_dictionary, 'c_is_fun')
        >>> print(new_dict)
        {'language': 'C', 'Number': 89, 'ids': [1, 2, 3]}
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
