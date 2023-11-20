#!/usr/bin/python3
"""
Unittests for FileStorage class
"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Testcase for filestorage"""
    @classmethod
    def setUpClass(cls):
        """A function that sets up tests"""
        cls.rev1 = Review()
        cls.rev1.place_id = "Nairobi"
        cls.rev1.user_id = "Jerry"
        cls.rev1.text = "Class B"
    @classmethod
    def tearDown(cls):
        """A function that tears down tests"""
        del cls.rev1

    def teardown(self):
        """A function that tears down tests"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """Tests for styles"""
        style = pep8.StyleGuide(quite=True)
        p = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """Tests all classes"""
        storage = FileStorage()
        ins_dic = storage.all()
        self.assertIsNotNone(ins_dic)
        self.assertEqual(type(ins_dic), dict)
        self.assertIs(ins_dic, storage._FileStorage__objects)

    def test_new(self):
        """Testing new methods"""
        m_storage = FileStorage()
        ins_dic = m_storage.all()
        mel = User()
        mel.id = 303033
        mel.name = "Mel"
        m_storage.new(mel)
        key = mel.__class__.__name__ + "." + str(mel.id)
        self.assertIsNotNone(ins_dic[key])

    def test_load(self):
        """Reloads tests"""
        a_storage = FileStorage()
        try:
            os.remove("file.json")
        except:
            pass
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(a_storage.reload(), None)
