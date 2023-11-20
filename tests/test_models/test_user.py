#!/usr/bin/python3
"""
Unittests for User
"""
import unittest
import os
import pep8
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Class tests for user """
    @classmethod
    def setUpClass(cls):
        """Sets up the class user"""
        cls.my_user = User()
        cls.my_user.first_name = "Deey"
        cls.my_user.last_name = "Kerry"
        cls.my_user.email = "dkerry@gmail.com"
        cls.my_user.password = "root"
    @classmethod
    def tearDownClass(cls):
        """Tears down the class"""
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests for styles"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/user.py'])
        self.assertEqual(p.total_errors, 2 != True, "fix pep8")

    def test_is_subclass(self):
        """Tests for the subclass"""
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Checks for functions of class"""
        self.assertIsNotNone(User.__doc__)

    def test_has_attributes(self):
        """Tests the has attributes of class"""
        self.assertTrue('email' in self.my_user.__dict__)
        self.assertTrue('id' in self.my_user.__dict__)
        self.assertTrue('created_at' in self.my_user.__dict__)
        self.assertTrue('updated_at' in self.my_user.__dict__)
        self.assertTrue('password' in self.my_user.__dict__)
        self.assertTrue('first_name' in self.my_user.__dict__)
        self.assertTrue('last_name' in self.my_user.__dict__)

    def test_attributes_are_strings(self):
        """Tests Attributes"""
        self.assertEqual(type(self.my_user.email), str)
        self.assertEqual(type(self.my_user.password), str)
        self.assertEqual(type(self.my_user.first_name), str)
        self.assertEqual(type(self.my_user.first_name), str)

    def test_save(self):
        """Saves tests"""
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    def test_to_dict(self):
        """Tests the dictionary"""
        self.assertEqual('to_dict' in dir(self.my_user), True)


if __name__ == "__main__":
    unittest.main()
