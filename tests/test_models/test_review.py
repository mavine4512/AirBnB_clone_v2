#!/usr/bin/python3
"""
Unittests for Review class
"""
import unittest
import os
import pep8
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests for the Review class"""
    @classmethod
    def setUpClass(cls):
        """Sets up the class"""
        cls.rev1 = Review()
        cls.rev1.place_id = "Raleigh"
        cls.rev1.user_id = "Greg"
        cls.rev1.text = "Grade A"

    @classmethod
    def tearDownClass(cls):
        """Tears the class down"""
        del cls.rev1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests for style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/review.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Tests for the subclass of main class
        """
        self.assertTrue(issubclass(self.rev1.__class__, BaseModel), True)

    def test_checking_for_functions(self):
        """Checks for functions"""
        self.assertIsNotNone(Review.__doc__)

    def test_has_attributes(self):
        """Tests the has attributes"""
        self.assertTrue('id' in self.rev1.__dict__)
        self.assertTrue('created_at' in self.rev1.__dict__)
        self.assertTrue('updated_at' in self.rev1.__dict__)
        self.assertTrue('place_id' in self.rev1.__dict__)
        self.assertTrue('text' in self.rev1.__dict__)
        self.assertTrue('user_id' in self.rev1.__dict__)

    def test_attributes_are_strings(self):
        """
        Tests the attributes of class
        """
        self.assertEqual(type(self.rev1.text), str)
        self.assertEqual(type(self.rev1.place_id), str)
        self.assertEqual(type(self.rev1.user_id), str)

    def test_save(self):
        """Saves the tests"""
        self.rev1.save()
        self.assertNotEqual(self.rev1.created_at, self.rev1.updated_at)

    def test_to_dict(self):
        """Tests the dictionary"""
        self.assertEqual('to_dict' in dir(self.rev1), True)


if __name__ == "__main__":
    unittest.main()
