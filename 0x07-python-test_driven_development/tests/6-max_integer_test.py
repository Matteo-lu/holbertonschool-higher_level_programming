#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerMethods(unittest.TestCase):
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
