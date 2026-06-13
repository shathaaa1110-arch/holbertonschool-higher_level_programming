#!/usr/bin/python3
"""
Module: 3-common_elements
Returns a set of common elements in two sets.
"""


def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.
Args:
        set_1: First set
        set_2: Second set

Returns:
        A new set containing only the elements that are in both sets.

Example:
        >>> set_1 = {"Python", "C", "Javascript"}
        >>> set_2 = {"Bash", "C", "Ruby", "Perl"}
        >>> c_set = common_elements(set_1, set_2)
        >>> print(sorted(list(c_set)))
        ['C']
    """
    return set_1 & set_2
