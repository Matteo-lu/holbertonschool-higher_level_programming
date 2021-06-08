#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
from models.square import Square


class TestRectangleClass(unittest.TestCase):
    """Test class to test Rectangle class"""

    @classmethod
    def setUpClass(self):
        """
        setUp class to import modules

        Args:
            None
        """

    def setUp(self):
        """
        setUp method to import modules

        Args:
            None
        """
        pass

    def test_Module_documentation(self):
        """
        testing module documentation

        Args:
            None
        """
        import models.square
        mod_doc = (models.square.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 4)

    def test_Class_documentation(self):
        """
        testing class documentation

        Args:
            None
        """
        class_doc = Square.__doc__
        self.assertTrue(len(class_doc.splitlines()) > 4)

    def test_shebang(self):
        """
        testing shebang

        Args:
            None
        """
        with open("models/square.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style

        Args:
            None
        """
        import os
        with os.popen("pep8 models/square.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_constructor(self):
        """
        test instanses of rectangle class

        Args:
            None
        """
        s1 = Square(5)
        s2 = Square(2, 2)
        s3 = Square(3, 1, 3)

        """Testing arguments"""
        self.assertEqual(s1.id, 22)
        self.assertEqual(s2.id, 23)
        self.assertEqual(s3.id, 24)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)

        """Testing area"""
        self.assertEqual(s1.area(), 25)
        self.assertEqual(s2.area(), 4)
        self.assertEqual(s3.area(), 9)

        """Testing __str__ method"""
        self.assertEqual(str(s1), "[Square] (22) 0/0 - 5")
        self.assertEqual(str(s2), "[Square] (23) 2/0 - 2")
        self.assertEqual(str(s3), "[Square] (24) 1/3 - 3")

        """Testing args update method"""
        s1.update()
        self.assertEqual(s1.id, 22)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        s1.update(89)
        self.assertEqual(s1.id, 89)
        s1.update(89, 2)
        self.assertEqual(s1.width, 2)
        s1.update(89, 2, 3)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 0)
        s1.update(89, 2, 3, 4)
        self.assertEqual(s1.y, 4)
        s1.update(89, 2, 3, 4, 5, 8, 13)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)

        """Testing kwargs update method"""
        s1 = Square(10, 10, 10, 10)

        s1.update()
        self.assertEqual(s1.id, 10)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.height, 10)
        s1.update(size=1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.size, 1)
        s1.update(size=1, x=2)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.x, 2)
        s1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.height, 2)
        self.assertEqual(s1.width, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 1)

        s1 = Square(10, 10, 10, 10)
        s1.update(1, size=2, y=3, id=4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.width, 10)
        self.assertEqual(s1.x, 10)
        self.assertEqual(s1.y, 10)
        self.assertEqual(s1.height, 10)

    def test_dict(self):
        """
        test dict object

        Args:
            None
        """
        s1 = Square(10, 2, 1, 1)
        self.assertEqual(s1.to_dictionary(), {'id': 1, 'size': 10, 'x': 2, 'y': 1})
        self.assertEqual(type(s1.to_dictionary()), dict)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(s2.id, 1)
        self.assertEqual(s2.size, 10)
        self.assertEqual(s2.x, 2)
        self.assertEqual(s2.y, 1)
        self.assertFalse((s1 == s2))

        s1 = Square(10)
        self.assertEqual(s1.to_dictionary(), {'id': 26, 'size': 10, 'x': 0, 'y': 0})
        r2 = Square(10, 2)
        self.assertEqual(r2.to_dictionary(), {'id': 27, 'size': 10, 'x': 2, 'y': 0})
        r2 = Square(10, 2, 15)
        self.assertEqual(r2.to_dictionary(), {'id': 28, 'size': 10, 'x': 2, 'y': 15})

    def test_setter_exceptions(self):
        """
        test setter exceptions for Square class

        Args:
            None
        """
        with self.assertRaises(TypeError) as types:
            Square([2], 2)
        self.assertEqual('width must be an integer', str(types.exception))

        with self.assertRaises(TypeError) as types:
            Square(10, "2")
        self.assertEqual('x must be an integer', str(types.exception))

        with self.assertRaises(ValueError) as value:
            Square(-10, 2)
        self.assertEqual('width must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            Square(10, -2)
        self.assertEqual('x must be >= 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            s = Square(10, 2)
            s.width = -10
        self.assertEqual('width must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            s = Square(10, 2)
            s.height = -10
        self.assertEqual('height must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            s = Square(0, 2)
        self.assertEqual('width must be > 0', str(value.exception))

        with self.assertRaises(TypeError) as types:
            s = Square(10, 2)
            s.x = {}
        self.assertEqual('x must be an integer', str(types.exception))

        with self.assertRaises(TypeError) as value:
            s = Square(10, 2)
            s.y = []
        self.assertEqual('y must be an integer', str(value.exception))

        with self.assertRaises(ValueError) as value:
            s = Square(10, 2, -3, 5)
        self.assertEqual('y must be >= 0', str(value.exception))

    def test_general_exceptions(self):
        """
        test general exceptions for rectangle class

        Args:
            None
        """
        with self.assertRaises(TypeError):
            s = Square()

if __name__ == '__main__':
    unittest.main()
