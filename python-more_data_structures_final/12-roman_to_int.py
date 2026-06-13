#!/usr/bin/python3
"""
Module: 12-roman_to_int
Converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.
    
    Args:
        roman_string: A string representing a Roman numeral
    
    Returns:
        An integer representing the value of the Roman numeral.
        If roman_string is not a string or None, return 0.
        The number will be between 1 to 3999.
    
    Roman numeral values:
        I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000
    
    Rules:
        - Generally, symbols are written from largest to smallest, left to right.
        - If a smaller value appears before a larger value, it is subtracted.
        - Examples: IV = 4 (5-1), IX = 9 (10-1), XL = 40 (50-10), XC = 90 (100-10)
    
    Example:
        >>> roman_to_int("X")
        10
        >>> roman_to_int("VII")
        7
        >>> roman_to_int("IX")
        9
        >>> roman_to_int("LXXXVII")
        87
        >>> roman_to_int("DCCVII")
        707
    """
    if not isinstance(roman_string, str):
        return 0
    
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    for i in range(len(roman_string)):
        # If current value is less than next value, subtract it (e.g., IV = 4)
        if (i + 1 < len(roman_string) and
                roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]):
            total -= roman_values[roman_string[i]]
        else:
            total += roman_values[roman_string[i]]
    
    return total
