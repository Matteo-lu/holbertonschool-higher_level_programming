#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxIntegerMethods(unittest.TestCase):
    """Exceptions are documented in the same way as classes.

    The __init__ method may be documented in either the class level
    docstring, or as a docstring on the __init__ method itself.

    Either form is acceptable, but the two should not be mixed. Choose one
    convention to document the __init__ method and be consistent with it.

    Note:
        Do not include the `self` parameter in the ``Args`` section.

    Args:
        msg (str): Human readable string describing the exception.
        code (:obj:`int`, optional): Error code.

    Attributes:
        msg (str): Human readable string describing the exception.
        code (int): Exception error code.

    """
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([-8, -7, -2, 0]), 0)
        self.assertEqual(max_integer([0]), 0)
        self.assertEqual(max_integer([-756]), -756)
        self.assertEqual(max_integer([1.1, 2.2, 4.4, 6.6]), 6.6)

    def test_string_type(self):
        self.assertRaises(TypeError, max_integer("h"))

    def tes_string(self):
        self.assertRaises(TypeError, max_integer([1, "h", 3, 4]))

if __name__ == '__main__':
    unittest.main()
