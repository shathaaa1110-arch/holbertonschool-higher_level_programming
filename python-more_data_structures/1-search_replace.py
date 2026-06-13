#!/usr/bin/python3
"""
Module: 1-search_replace
Replaces all occurrences of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list: The initial list
        search: The element to replace in the list
        replace: The new element

    Returns:
        A new list with all occurrences of 'search' replaced by 'replace'.
        The initial list is not modified.

    Example:
        >>> my_list = [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
        >>> new_list = search_replace(my_list, 2, 89)
        >>> print(new_list)
        [1, 89, 3, 4, 5, 4, 89, 1, 1, 4, 89]
        >>> print(my_list)
        [1, 2, 3, 4, 5, 4, 2, 1, 1, 4, 89]
    """
    return [replace if i == search else i for i in my_list]
