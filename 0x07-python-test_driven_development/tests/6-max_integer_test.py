#!/usr/bin/python3
"""Unittest for 6-max_integer module
"""

import unittest
"""
Uniittest module contains various testcases for asserting functions returm
expected values
"""

max_integer = __import__("6-max_integer").max_integer
"""
Contains only one function: max_integer. Used to find the largest integer
in a list
"""


class TestMaxInteger(unittest.TestCase):
    """Tests 6-max_integer module

    Attributes:
    None

    """

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([0, 0, 0]), 0)
        self.assertEqual(max_integer([567789, 54, 0, -67, 125, 567789]), 567789)
        self.assertEqual(max_integer([-6, 0, -78, -34, -78]), 0)
        self.assertEqual(max_integer([45]), 45)
        self.assertEqual(max_integer([]), None)
