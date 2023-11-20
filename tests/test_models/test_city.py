#!/usr/bin/python3
"""Unittest for city class"""
import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests for City class"""
    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city1.name = "Nairobi"
        cls.city1.state_id = "NB"
    @classmethod
    def tearDownClass(cls):
        """Tears down class"""
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests styles"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
        
    def test_is_subclass(self):
        """
        Tests subclass
        """
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Checks for functions"""
        self.assertIsNotNone(City.__doc__)

    def test_has_attributes(self):
        """Tests attributes"""
        self.assertTrue('id' in self.city1.__dict__)
        self.assertTrue('created_at' in self.city1.__dict__)
        self.assertTrue('updated_at' in self.city1.__dict__)
        self.assertTrue('state_id' in self.city1.__dict__)
        self.assertTrue('name' in self.city1.__dict__)

    def test_attributes_are_strings(self):
        """
        Tests attributes that are strings
        """
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        """Saves tests"""
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """
        Tests the dictionary
        """
        self.assertEqual('to_dict' in dir(self.city1), True)


if __name__ == "__main__":
    unittest.main()
