#!/usr/bin/env python3
"""Defines a custom list class that prints notifications."""


class VerboseList(list):
    """A list that notifies when items are added or removed."""

    def append(self, item):
        """Add an item to the end of the list."""
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, iterable):
        """Extend the list with items from an iterable."""
        count = len(iterable)
        super().extend(iterable)
        print("Extended the list with [{}] items.".format(count))

    def remove(self, item):
        """Remove the first occurrence of an item from the list."""
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Remove and return an item at the given index."""
        item = self[index]
        print("Popped [{}] from the list.".format(item))
        return super().pop(index)
