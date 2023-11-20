#!/usr/bin/python3
"""
Unittests for State class
"""
import unittest
import os
import pep8
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests for the class State"""
    @classmethod
    def setUpClass(cls):
        """Sets up the class"""
        cls.state1 = State()
        cls.state1.name = "KASARANI"
    @classmethod
    def tearDownClass(cls):
        """
        Tears down the class
        """
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests for the style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/state.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """Tests for the subclass"""
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Checks for the function tests"""
        self.assertIsNotNone(State.__doc__)

    def test_has_attributes(self):
        """Tests the has attributes"""
        self.assertTrue('id' in self.state1.__dict__)
        self.assertTrue('created_at' in self.state1.__dict__)
        self.assertTrue('updated_at' in self.state1.__dict__)
        self.assertTrue('name' in self.state1.__dict__)

    def test_attributes_are_strings(self):
        """
        Tests the attributes
        """
        self.assertEqual(type(self.state1.name), str)

    def test_save(self):
        """Saves the tests"""
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_to_dict(self):
        """Tests the dictionary"""
        self.assertEqual('to_dict' in dir(self.state1), True)


if __name__ == "__main__":
    unittest.main()
