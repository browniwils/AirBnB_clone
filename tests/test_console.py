#!/usr/bin/python3
"""
Program for Unit test for the file storage class
"""
import os, json, unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsoleClass(unittest.TestCase):
    """
    Test for console
    """
    maxDiff = None
    file_path = "test.json"
    storage = FileStorage(file_path)

    def setUp(self):
        """ condition to test file saving """
        self.storage.save()

    def tearDown(self):
        """ destroys created file """
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_check_help(self):
        """ test command if it has a help output """
        with patch('sys.stdout', new=StringIO()) as help_content:
            HBNBCommand().onecmd("help create")
            self.assertTrue(len(help_content.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_content:
            HBNBCommand().onecmd("help all")
            self.assertTrue(len(help_content.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_content:
            HBNBCommand().onecmd("help show")
            self.assertTrue(len(help_content.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_content:
            HBNBCommand().onecmd("help destroy")
            self.assertTrue(len(help_content.getvalue()) > 0)
        with patch('sys.stdout', new=StringIO()) as help_content:
            HBNBCommand().onecmd("help update")
            self.assertTrue(len(help_content.getvalue()) > 0)

    def test_create(self):
        """ Test for creating """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(content.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create")
            self.assertEqual(content.getvalue(), "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create Holberton")
            self.assertEqual(content.getvalue(), "** class doesn't exist **\n")

    def test_show(self):
        """ test for object show """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('create BaseModel')
            id = content.getvalue()
            self.assertTrue(len(id) > 0)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("{} {}".format("show BaseModel", id))
            self.assertTrue(content.getvalue() != "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('show helloo ')
            self.assertTrue(content.getvalue() == "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('show')
            self.assertTrue(content.getvalue() == "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('show BaseModel')
            self.assertTrue(content.getvalue() == "** instance id missing **\n")

    def test_destroy(self):
        """ test for destroy object """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('destroy')
            self.assertTrue(content.getvalue() == "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('destroy fakeclass')
            self.assertTrue(content.getvalue() == "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('destroy BaseModel')
            self.assertTrue(content.getvalue() == "** instance id missing **\n")
    
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('destroy BaseModel 121212')
            self.assertTrue(content.getvalue() == "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('create BaseModel')
            id = content.getvalue()
            self.assertTrue(len(id) > 0)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("{} {}".format("destroy BaseModel", id))
            self.assertTrue(content.getvalue() != "** no instance found **\n")

    def test_all(self):
        """ test for all """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('create BaseModel')
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('all FakeClass')
            self.assertTrue(content.getvalue() == "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('all')
            self.assertTrue(len(content.getvalue()) > 0)

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('all BaseModel')
            self.assertTrue(len(content.getvalue()) > 0)

    def test_update(self):
        """ test for update """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('update')
            self.assertTrue(content.getvalue() == "** class name missing **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('update FakeClass')
            self.assertTrue(content.getvalue() == "** class doesn't exist **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('update BaseModel')
            self.assertTrue(content.getvalue() == "** instance id missing **\n")
    
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('update BaseModel 121212')
            self.assertTrue(content.getvalue() == "** no instance found **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd('create BaseModel')
            id = content.getvalue()
            self.assertTrue(len(id) > 0)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("{} {}".format("update BaseModel", id))
            self.assertTrue(content.getvalue() == "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("{} {} {}".format("update BaseModel", id, "first_name"))
            self.assertTrue(content.getvalue() == "** value missing **\n")

        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("{} {} {}".format("update BaseModel", id, "name betty"))
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("{} {}".format("show BaseModel", id))
            self.assertTrue("betty" in content.getvalue())

    def test_user(self):
        """ Test for user """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
            id = content.getvalue()
            self.assertTrue(id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show User " + id)
            self.assertTrue(content.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("all User")
            self.assertTrue(content.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("update User " + id + " name betty")
            HBNBCommand().onecmd("show User " + id)
            self.assertTrue("betty" in content.getvalue())
            HBNBCommand().onecmd("destroy User " + id)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show User "+id)
            self.assertEqual(content.getvalue(), "** no instance found **\n")

    def test_place(self):
        """ Test place """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create Place")
            id = content.getvalue()
            self.assertTrue(id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show Place " + id)
            self.assertTrue(content.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("all Place")
            self.assertTrue(content.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("update Place " + id + " name betty")
            HBNBCommand().onecmd("show Place " + id)
            self.assertTrue("betty" in content.getvalue())
            HBNBCommand().onecmd("destroy Place " + id)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show Place "+id)
            self.assertEqual(content.getvalue(), "** no instance found **\n")

    def test_state(self):
        """ Test for state """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create State")
            id = content.getvalue()
            self.assertTrue(id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show State " + id)
            self.assertTrue(content.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("all State")
            self.assertTrue(content.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("update State " + id + " name betty")
            HBNBCommand().onecmd("show State " + id)
            self.assertTrue("betty" in content.getvalue())
            HBNBCommand().onecmd("destroy State " + id)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show State "+id)
            self.assertEqual(content.getvalue(), "** no instance found **\n")

    def test_city(self):
        """ Test for city """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create City")
            id = content.getvalue()
            self.assertTrue(id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show City " + id)
            self.assertTrue(content.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("all City")
            self.assertTrue(content.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("update City " + id + " name betty")
            HBNBCommand().onecmd("show City " + id)
            self.assertTrue("betty" in content.getvalue())
            HBNBCommand().onecmd("destroy City " + id)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show City "+id)
            self.assertEqual(content.getvalue(), "** no instance found **\n")

    def test_amenity(self):
        """ Test for amenity """
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create Amenity")
            id = content.getvalue()
            self.assertTrue(id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show Amenity " + id)
            self.assertTrue(content.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("all Amenity")
            self.assertTrue(content.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("update Amenity " + id + " name betty")
            HBNBCommand().onecmd("show Amenity " + id)
            self.assertTrue("betty" in content.getvalue())
            HBNBCommand().onecmd("destroy Amenity " + id)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("show Amenity "+id)
            self.assertEqual(content.getvalue(), "** no instance found **\n")

    def test_review(self):
        """ Test for review """
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("create Review")
            id = val.getvalue()
            self.assertTrue(id != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review " + id)
            self.assertTrue(val.getvalue() != "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("all Review")
            self.assertTrue(val.getvalue() != "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("update Review " + id + " name betty")
            HBNBCommand().onecmd("show Review " + id)
            self.assertTrue("betty" in val.getvalue())
            HBNBCommand().onecmd("destroy Review " + id)
        with patch('sys.stdout', new=StringIO()) as val:
            HBNBCommand().onecmd("show Review "+id)
            self.assertEqual(val.getvalue(), "** no instance found **\n")

    def test_advance_all(self):
        """test advance all with [class].all"""
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.all()")
            self.assertTrue(len(content.getvalue()) > 0)

    def test_advance_show(self):
        """test advance show with [class].show"""
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
            id = content.getvalue()
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.show(\"" + id + "\")")
            self.assertTrue(len(content.getvalue()) > 0)

    def test_count(self):
        """test advance show with [class].show"""
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(content.getvalue()) == 0)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(content.getvalue()) == 1)

    def test_advance_destroy(self):
        """test advance destroy with [class].destroy(id)"""
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
            id = content.getvalue()
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.destroy(\"" + id + "\")")
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.count()")
            self.assertTrue(int(content.getvalue()) == 0)

    def test_advance_update1(self):
        """test advance update with [class].show"""
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
            id = content.getvalue()
        with patch('sys.stdout', new=StringIO()) as content:
            line = "\", \"name\", \"betty\")"
            HBNBCommand().onecmd("User.update(\"" + id + line)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.show(\"" + id + "\")")
            self.assertTrue("betty" in content.getvalue())

    def test_advance_update2(self):
        """test advance update with [class].show"""
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("create User")
            id = content.getvalue()
        with patch('sys.stdout', new=StringIO()) as content:
            line = "\", {'first_name': 'John', 'age': 89})"
            HBNBCommand().onecmd("User.update(\"" + id + line)
        with patch('sys.stdout', new=StringIO()) as content:
            HBNBCommand().onecmd("User.show(\"" + id + "\")")
            self.assertTrue("John" in content.getvalue())

if __name__ == '__main__':
    unittest.main()