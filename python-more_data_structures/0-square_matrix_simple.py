#!/usr/bin/python3
"""
Module: 0-square_matrix_simple
Computes the square value of all integers of a matrix.
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.
    
    Args:
        matrix: A 2 dimensional array (list of lists)
    
    Returns:
        A new matrix with the same size where each value is squared.
        The initial matrix is not modified.
    
    Example:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> new_matrix = square_matrix_simple(matrix)
        >>> print(new_matrix)
        [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
        >>> print(matrix)
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [[i ** 2 for i in row] for row in matrix]
