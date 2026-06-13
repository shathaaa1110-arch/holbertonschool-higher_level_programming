#!/usr/bin/python3
"""
Module: 11-multiply_list_map
Returns a list with all values multiplied by a number without using loops.
"""


def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied by a number without loops.

    Args:
        my_list: The initial list
        number: The number to multiply by

    Returns:
        A new list with the same length where each value is multiplied.
        The initial list is not modified.

    Note:
        This function uses map() instead of loops.
        The file should be max 3 lines.

    Example:
        >>> my_list = [1, 2, 3, 4, 6]
        >>> new_list = multiply_list_map(my_list, 4)
        >>> print(new_list)
        [4, 8, 12, 16, 24]
    """
    return list(map(lambda x: x * number, my_list))

