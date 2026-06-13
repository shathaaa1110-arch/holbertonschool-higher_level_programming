#!/usr/bin/python3
"""
Module: 4-only_diff_elements
Returns a set of all elements present in only one set.
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1: First set
        set_2: Second set

    Returns:
        A new set containing elements that are in set_1 or set_2
        but not in both. This is the symmetric difference of the two sets.

    Example:
        >>> set_1 = {"Python", "C", "Javascript"}
        >>> set_2 = {"Bash", "C", "Ruby", "Perl"}
        >>> od_set = only_diff_elements(set_1, set_2)
        >>> print(sorted(list(od_set)))
        ['Bash', 'Javascript', 'Perl', 'Python', 'Ruby']
    """
    return (set_1 - set_2) | (set_2 - set_1)
    
