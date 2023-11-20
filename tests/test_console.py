#!/usr/bin/python3
"""Unittests Function module that tests HBNB for all classes"""
import unittest
from unittest.mock import patch
from io import StringIO
import pep8
import os
import json
import console
import tests
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """Function that test for HBNB command in all classes"""
    @classmethod
    def setUpClass(self):
        """Function that sets up test for all classes"""
        self.typing = console.HBNBCommand()

    @classmethod
    def tearDownClass(self):
        """Function that bring down a class"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_console(self):
        """The console"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_pep8_test_console(self):
        """The console"""
        style = pep8.StyleGuide(quiet=False)
        errors = 0
        file = (["tests/test_console.py"])
        errors += style.check_files(file).total_errors
        self.assertEqual(errors, 0, 'Need to fix Pep8')

    def test_docstrings_in_console(self):
        """Doc strings in a class"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_docstrings_in_test_console(self):
        """Doc strings in a class"""
        self.assertTrue(len(console.__doc__) >= 1)

    def test_emptyline(self):
        """Tests for an empty line"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("\n")
            self.assertEqual(fake_output.getvalue(), '')

    def test_create(self):
        """Creates new tests"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create SomeClass")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("create User")
            self.typing.onecmd("crete User")
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.all()")
            self.assertEqual("[[User]",
                             fake_output.getvalue()[:7])

    def test_all(self):
        """Tests all output"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all NonExiststantModel")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("all Place")
            self.assertEqual("[]\n", fake_output.getvalue())

    def test_destroy(self):
        """Destroys all output"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy Theworld")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("destroy BaseModel 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("City.destroy('123')")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_update(self):
        """Updates tests"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update You")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("update User 12345")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_show(self):
        """Shows tests"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show")
            self.assertEqual("** class name missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("SomeClass.show()")
            self.assertEqual("** class doesn't exist **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("show Review")
            self.assertEqual("** instance id missing **\n",
                             fake_output.getvalue())
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.show('123')")
            self.assertEqual("** no instance found **\n",
                             fake_output.getvalue())

    def test_class_cmd(self):
        """Class commands"""
        with patch('sys.stdout', new=StringIO()) as fake_output:
            self.typing.onecmd("User.count()")
            self.assertEqual(int, type(eval(fake_output.getvalue())))

if __name__ == "__main__":
    unittest.main()
