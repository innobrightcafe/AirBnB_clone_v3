#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""
import sys
import models
import unittest
from models import storage
from models import State
from models.engine.db_storage import DBStorage
from io import StringIO
from console import HBNBCommand
from unittest.mock import create_autospec
from os import getenv
import console
from models import state
from models.engine import db_storage, file_storage
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """Test that console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """Test that tests/test_console.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """Test for the HBNBCommand class docstring"""
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand class needs a docstring")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class needs a docstring")


class TestHBNBCommandDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('.......  For the Console  .......')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = ' Command interpreter for Holberton AirBnB project '
        actual = console.__doc__
        self.assertEqual(actual, expected)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = ' Command interpreter class '
        actual = HBNBCommand.__doc__
        self.assertEqual(actual, expected)


# class TestMethods(unittest.TestCase):
#     def test_get_existing_obj(self):
#         """check for get method on dbstorage"""
#         obj = state.State(name="California")
#         storage = db_storage.DBStorage()
#         storage.new(obj)
#         storage.save()
#         retrieved_obj = storage.get(state.State, obj.id)
#         self.assertEqual(obj, retrieved_obj)

    # def test_get_nonexistent_object(self):
    #     retrieved_obj = db_storage.DBStorage().get(state.State, "nonexistent-id")
    #     self.assertIsNone(retrieved_obj)

    # def test_count(self):
    #     """assuming there are two classes in the storage"""
    #     count = db_storage.DBStorage()
    #     self.assertEqual(count, 2)

class test_console(unittest.TestCase):
    """ Test the console module"""
    def setUp(self):
        """setup for"""
        self.backup = sys.stdout
        self.capt_out = StringIO()
        sys.stdout = self.capt_out

    def tearDown(self):
        """"""
        sys.stdout = self.backup

    def create(self):
        """ create an instance of the HBNBCommand class"""
        return HBNBCommand()

    def test_quit(self):
        """ Test quit exists"""
        console = self.create()
        self.assertTrue(console.onecmd("quit"))

    def test_EOF(self):
        """ Test EOF exists"""
        console = self.create()
        self.assertTrue(console.onecmd("EOF"))

    def test_all(self):
        """ Test all exists"""
        console = self.create()
        console.onecmd("all")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show(self):
        """
            Testing that show exists
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + user_id)
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertTrue(str is type(x))

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_class_name(self):
        """
            Testing the error messages for class name missing.
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** class name missing **\n", x)

    def test_show_class_name(self):
        """
            Test show message error for id missing
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** instance id missing **\n", x)

    @unittest.skipIf(db == "db", "Testing database storage only")
    def test_show_no_instance_found(self):
        """
            Test show message error for id missing
        """
        console = self.create()
        console.onecmd("create User")
        user_id = self.capt_out.getvalue()
        sys.stdout = self.backup
        self.capt_out.close()
        self.capt_out = StringIO()
        sys.stdout = self.capt_out
        console.onecmd("show User " + "124356876")
        x = (self.capt_out.getvalue())
        sys.stdout = self.backup
        self.assertEqual("** no instance found **\n", x)

    def test_create(self):
        """
            Test that create works
        """
        console = self.create()
        console.onecmd("create User email=adriel@hbnb.com password=abc")
        self.assertTrue(isinstance(self.capt_out.getvalue(), str))

    def test_class_name(self):
        """
            Testing the error messages for class name missing.
        """
        console = self.create()
        console.onecmd("create")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class name missing **\n", x)

    def test_class_name_doest_exist(self):
        """
            Testing the error messages for class name missing.

        """
        console = self.create()
        console.onecmd("create Binita")
        x = (self.capt_out.getvalue())
        self.assertEqual("** class doesn't exist **\n", x)

    @unittest.skipIf(db != 'db', "Testing DBstorage only")
    def test_create_db(self):
        console = self.create()
        console.onecmd("create State name=California")
        result = storage.all("State")
        self.assertTrue(len(result) > 0)


if __name__ == "__main__":
    unittest.main()
