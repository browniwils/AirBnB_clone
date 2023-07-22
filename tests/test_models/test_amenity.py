#!/usr/bin/python3
"""
Test for amenity
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test the Amenity
    """
    def test_is_subclass(self):
        """
        Test that Amenity is a subclass of BaseModel
        """
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """
        Test that Amenity has attribute name,
        and it's as an empty string
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        """
        test to_dict method creates a dictionary
        with pobject attributes
        """
        amenity = Amenity()
        new_d = amenity.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in amenity.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """
        test that values in dict returned from
        to_dict are correct
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity = Amenity()
        new_d = amenity.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], amenity.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], amenity.updated_at.strftime(t_format))

    def test_str(self):
        """
        test that the str method has the correct output
        """
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
