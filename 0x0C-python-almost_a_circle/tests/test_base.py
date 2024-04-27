#!/usr/bin/python3

"""
Imported module:

unittest & base
Test packages, modules, classes and methods/functions

base
Base class for 2d shapes
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Tests the base class module

    """
    def setUp(self):
        obj1 = Base(50)
        obj2 ° Base()
        obj3 = Base()

    def testConstructor(self):
        self.assertEqual(obj1.id, 50)
        self.assertEqual(obj2.id, 1)
        self.assertEqual(obj3.id, 2)
