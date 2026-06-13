#!/usr/bin/python3
"""
Module: 9-multiply_by_2
Returns a new dictionary with all values multiplied by 2.
"""


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.
    
    Args:
        a_dictionary: A dictionary with integer values
    
    Returns:
        A new dictionary where all values are multiplied by 2.
        The original dictionary is not modified.
    
    Example:
        >>> a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
        >>> new_dict = multiply_by_2(a_dictionary)
        >>> print(new_dict)
        {'John': 24, 'Alex': 16, 'Bob': 28, 'Mike': 28, 'Molly': 32}
        >>> print(a_dictionary)
        {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
    """
    return {k: v * 2 for k, v in a_dictionary.items()}
