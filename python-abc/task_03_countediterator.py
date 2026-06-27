#!/usr/bin/env python3
"""Defines an iterator that counts its steps."""


class CountedIterator:
    """An iterator that keeps track of the number of items fetched."""

    def __init__(self, iterable):
        """Initialize the counted iterator."""
        self.iterator = iter(iterable)
        self.counter = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Fetch the next item and increment the counter."""
        item = next(self.iterator)
        self.counter += 1
        return item

    def get_count(self):
        """Return the current value of the counter."""
        return self.counter
