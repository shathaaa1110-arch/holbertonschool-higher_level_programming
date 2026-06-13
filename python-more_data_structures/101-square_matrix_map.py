#!/usr/bin/python3
"""
Module: 101-square_matrix_map
Computes the square value of all integers of a matrix using map.
"""


def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers of a matrix using map.
    
    Args:
        matrix: A 2 dimensional array (list of lists)
    
    Returns:
        A new matrix with the same size where each value is squared.
        The initial matrix is not modified.
    
    Note:
        This function uses map() instead of loops.
        You are not allowed to use for or while loops.
        The file should be max 3 lines.
    
    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> new_matrix = square_matrix_map(matrix)
        >>> print(new_matrix)
        [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
        >>> print(matrix)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
