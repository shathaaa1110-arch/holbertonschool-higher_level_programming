#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_regular_list(self):
        """Max at the end."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_beginning(self):
        """Max at the start."""
        self.assertEqual(max_integer([9, 3, 4, 2]), 9)

    def test_max_in_middle(self):
        """Max in the middle."""
        self.assertEqual(max_integer([1, 7, 3, 2]), 7)

    def test_one_element(self):
        """Single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        """All negative numbers."""
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_mixed_negative_positive(self):
        """Mix of negative and positive."""
        self.assertEqual(max_integer([-1, 0, 5, -10]), 5)

    def test_equal_elements(self):
        """All elements equal."""
        self.assertEqual(max_integer([3, 3, 3]), 3)

    def test_floats(self):
        """Floating point numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_no_argument(self):
        """No argument — uses default empty list."""
        self.assertIsNone(max_integer())


if __name__ == '__main__':
    unittest.main()
