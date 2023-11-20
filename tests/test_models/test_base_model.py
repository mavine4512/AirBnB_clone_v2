#!/usr/bin/python3
"""Unittests for  BaseModel class"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Testcase for Base Model"""
    @classmethod
    def setUp(cls):
        """A function that sets up tests"""
        cls.base1 = BaseModel()
        cls.base1.name = "James"
        cls.base1.name = "30"
    @classmethod
    def tearDown(cls):
        """A function that tears down tests"""
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Tests for styles
        """
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")
    
    def test_checking_for_functions(self):
        """Checking for functions"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_has_attributes(self):
        """Test Attributes"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))
        

    def test_init(self):
        """Tests initialization"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        """Saves tests"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
        """Tests the dictionary"""
        base1_dict = self.base1.to_dict
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)


if __name__ == "__main__":
    unittest.main()

