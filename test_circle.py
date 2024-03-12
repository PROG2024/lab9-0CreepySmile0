"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
from circle import Circle
import unittest


class TestCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(3)

    def test_circle_constructor(self):
        with self.assertRaises(TypeError):
            x = Circle("7")
        with self.assertRaises(ValueError):
            x = Circle(-1)

    def test_add_area(self):
        c = Circle(4)
        new_c = self.circle.add_area(c)
        self.assertEqual(new_c.get_radius(), 5)

    def test_add_area_radius0(self):
        c = Circle(0)
        new_c = self.circle.add_area(c)
        self.assertEqual(new_c.get_radius(), 3)
