#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
from models.rectangle import Rectangle


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
        import models.rectangle
        mod_doc = (models.rectangle.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 4)

    def test_Class_documentation(self):
        """
        testing class documentation

        Args:
            None
        """
        class_doc = Rectangle.__doc__
        self.assertTrue(len(class_doc.splitlines()) > 4)

    def test_shebang(self):
        """
        testing shebang

        Args:
            None
        """
        with open("models/rectangle.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style

        Args:
            None
        """
        import os
        with os.popen("pep8 models/rectangle.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_constructor(self):
        """
        test instanses of rectangle class

        Args:
            None
        """
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 5, 0, 0, 12)
        r4 = Rectangle(3, 2)
        r5 = Rectangle(8, 10, 3, 5)

        """Testing arguments"""
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)
        self.assertEqual(r4.id, 3)
        self.assertEqual(r5.width, 8)
        self.assertEqual(r5.height, 10)
        self.assertEqual(r5.x, 3)
        self.assertEqual(r5.y, 5)
        self.assertEqual(r5.id, 4)

        """Testing aruments conditions"""
        r5.width = 15
        self.assertEqual(r5.width, 15)
        r5.height = 16
        self.assertEqual(r5.height, 16)
        r5.x = 17
        self.assertEqual(r5.x, 17)
        r5.y = 18
        self.assertEqual(r5.y, 18)

        """Testing area"""
        self.assertEqual(r1.area(), 20)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 50)
        self.assertEqual(r4.area(), 6)
        self.assertEqual(r5.area(), 240)

        """Testing __str__ method"""
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 10/2")
        self.assertEqual(str(r2), "[Rectangle] (2) 0/0 - 2/10")
        self.assertEqual(str(r3), "[Rectangle] (12) 0/0 - 10/5")
        self.assertEqual(str(r4), "[Rectangle] (3) 0/0 - 3/2")
        self.assertEqual(str(r5), "[Rectangle] (4) 17/18 - 15/16")

        """Testing args update method"""
        r1.update()
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r1.update(89)
        self.assertEqual(r1.id, 89)
        r1.update(89, 2)
        self.assertEqual(r1.width, 2)
        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)
        r1.update(89, 2, 3, 4, 5, 8, 13)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

        """Testing kwargs update method"""
        r1 = Rectangle(10, 10, 10, 10)

        r1.update()
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.height, 10)
        r1.update(height=1)
        self.assertEqual(r1.height, 1)
        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)
        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.id, 89)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 1)
        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.height, 2)

        r1 = Rectangle(10, 10, 10, 10)
        r1.update(1, height=2, y=3, width=4)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.height, 10)

    def test_setter_exceptions(self):
        """
        test setter exceptions for rectangle class

        Args:
            None
        """
        with self.assertRaises(TypeError) as types:
            Rectangle([2], 2)
        self.assertEqual('width must be an integer', str(types.exception))

        with self.assertRaises(TypeError) as types:
            Rectangle(10, "2")
        self.assertEqual('height must be an integer', str(types.exception))

        with self.assertRaises(TypeError) as types:
            r = Rectangle(10, 2)
            r.width = "2"
        self.assertEqual('width must be an integer', str(types.exception))

        with self.assertRaises(TypeError) as types:
            r = Rectangle(10, 2)
            r.height = [2]
        self.assertEqual('height must be an integer', str(types.exception))

        with self.assertRaises(ValueError) as value:
            Rectangle(-10, 2)
        self.assertEqual('width must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            Rectangle(10, -2)
        self.assertEqual('height must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            r = Rectangle(10, 2)
            r.width = -10
        self.assertEqual('width must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            r = Rectangle(10, 2)
            r.height = -10
        self.assertEqual('height must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            r = Rectangle(0, 2)
        self.assertEqual('width must be > 0', str(value.exception))

        with self.assertRaises(ValueError) as value:
            r = Rectangle(10, 0)
        self.assertEqual('height must be > 0', str(value.exception))

        with self.assertRaises(TypeError) as types:
            r = Rectangle(10, 2)
            r.x = {}
        self.assertEqual('x must be an integer', str(types.exception))

        with self.assertRaises(ValueError) as value:
            r = Rectangle(10, 2, 3, -1)
        self.assertEqual('y must be >= 0', str(value.exception))

        with self.assertRaises(TypeError) as value:
            r = Rectangle(10, 2)
            r.y = []
        self.assertEqual('y must be an integer', str(value.exception))

        with self.assertRaises(ValueError) as value:
            r = Rectangle(10, 2, -3, 5)
        self.assertEqual('x must be >= 0', str(value.exception))

    def test_general_exceptions(self):
        """
        test general exceptions for rectangle class

        Args:
            None
        """
        with self.assertRaises(TypeError):
            r = Rectangle()

        with self.assertRaises(TypeError):
            r = Rectangle(8)

if __name__ == '__main__':
    unittest.main()
