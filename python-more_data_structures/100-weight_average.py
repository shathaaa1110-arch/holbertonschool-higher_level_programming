#!/usr/bin/python3
"""
Module: 100-weight_average
Returns the weighted average of all integers tuple (<score>, <weight>).
"""


def weight_average(my_list=[]):
    """
    Returns the weighted average of all integers tuple (<score>, <weight>).

    Args:
        my_list: A list of tuples where each tuple is (<score>, <weight>)

    Returns:
        The weighted average as a float.
        If the list is empty, return 0.

    Formula:
        Weighted Average = (sum of (score * weight)) / (sum of all weights)

    Example:
        >>> my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
        >>> # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
        >>> # = (2 + 2 + 30 + 8) / 15
        >>> # = 42 / 15
        >>> # = 2.8
        >>> result = weight_average(my_list)
        >>> print("Average: {:0.2f}".format(result))
        Average: 2.80
    """
    if not my_list:
        return 0

    total_score = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)

    return total_score / total_weight
