#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
import models.base
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Test class to test Base class"""

    def test_Module_documentation(self):
        """
        testing module documentation

        Args:
            None
        """
        mod_doc = (models.base.__doc__)
        self.assertTrue(len(mod_doc.strip().splitlines()) >= 4)

    def test_Class_documentation(self):
        """
        testing class documentation

        Args:
            None
        """
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc.splitlines()) > 4)

    def test_shebang(self):
        """
        testing shebang

        Args:
            None
        """
        with open("models/base.py", "r") as file:
            first_line = file.readline()
            self.assertTrue(first_line.strip() == "#!/usr/bin/python3")

    def test_style(self):
        """
        testing pep8 style

        Args:
            None
        """
        import os
        with os.popen("pep8 models/base.py") as my_file:
            self.assertEqual(my_file.read(), '')

    def test_constructor(self):
        """
        test instanses of base class

        Args:
            None
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        b6 = Base(-9)
        b7 = Base(0)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
        self.assertEqual(b6.id, -9)
        self.assertEqual(b7.id, 0)

    def test_json_string(self):
        """
        test json string

        Args:
            None
        """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        self.assertEqual(type(Base.to_json_string([dictionary])), str)

        self.assertEqual(Base.to_json_string(None), "[]")

        self.assertEqual(Base.to_json_string([]), "[]")

    """def test_save_to_file(self):
        test instanses of base class

        Args:
            None
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            ret = file.read()
        self.assertEqual(ret, second)"""

    def test_from_json_string(json_string):
        """
        test json string

        Args:
            None
        """

if __name__ == '__main__':
    unittest.main()
