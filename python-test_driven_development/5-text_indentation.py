#!/usr/bin/python3
"""
This module contains a function that indents text.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 1:
            if char == " ":
                continue
            flag = 0
        print(char, end="")
        if char in ".?:":
            print("\n")
            flag = 1
    print()
