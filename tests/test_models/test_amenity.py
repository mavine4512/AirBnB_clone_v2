#!/usr/bin/python3
"""
Unittests for Amenity class
"""
import unittest
import os
import pep8
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Ceates the tests for Amenity"""
    @classmethod
    def setUpClass(cls):
        """Sets up class"""
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Toilet Sink"
    @classmethod
    def tearDownClass(cls):
        """Tears down the class"""
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests for styles"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/amenity.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Tests for subclass in main class
        """
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Checks for functions"""
        self.assertIsNotNone(Amenity.__doc__)

    def test_has_attributes(self):
        """Tests has attributes"""
        self.assertTrue('id' in self.amenity1.__dict__)
        self.assertTrue('created_at' in self.amenity1.__dict__)
        self.assertTrue('updated_at' in self.amenity1.__dict__)
        self.assertTrue('name' in self.amenity1.__dict__)

    def test_attributes_are_strings(self):
        """
        Tests the attributes of the module
        """
        self.assertEqual(type(self.amenity1.name), str)

    def test_save(self):
        """ Saves the tests"""
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at)

    def test_to_dict(self):
        """
        Tests the dictionary
        """
        self.assertEqual('to_dict' in dir(self.amenity1), True)


if __name__ == "__main__":
    unittest.main()
