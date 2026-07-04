#!/usr/bin/python3
"""Module that inserts a line after lines containing a given string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert a line after each line containing search_string."""
    lines = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as file:
        file.writelines(lines)
