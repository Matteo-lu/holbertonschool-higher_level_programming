#!/usr/bin/python3
"""Unittest for Base class
"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """Test class to test Base class"""

    @classmethod
    def setUpClass(self):"""
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
        import models.base
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

if __name__ == '__main__':
    unittest.main()
