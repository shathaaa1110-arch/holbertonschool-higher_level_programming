#!/usr/bin/env python3
"""Defines a Dragon class using mixins."""


class SwimMixin:
    """A mixin for swimming behavior."""

    def swim(self):
        """Print swimming message."""
        print("The creature swims!")


class FlyMixin:
    """A mixin for flying behavior."""

    def fly(self):
        """Print flying message."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a dragon with multiple abilities."""

    def roar(self):
        """Print roaring message."""
        print("The dragon roars!")
