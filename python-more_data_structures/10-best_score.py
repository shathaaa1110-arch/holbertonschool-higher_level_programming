#!/usr/bin/python3
"""
Module: 10-best_score
Returns a key with the biggest integer value.
"""


def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary: A dictionary with integer values

    Returns:
        The key with the biggest value.
        If no score found or dictionary is None/empty, return None.

    Example:
        >>> a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
        >>> best_key = best_score(a_dictionary)
        >>> print("Best score: {}".format(best_key))
        Best score: Molly

        >>> best_key = best_score(None)
        >>> print("Best score: {}".format(best_key))
        Best score: None
    """
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    return max(a_dictionary, key=a_dictionary.get)
