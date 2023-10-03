#!/usr/bin/python3
"""
Test for city
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """
        Test that City is a subclass of BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_name_attr(self):
        """
        Test that City has attribute name, and it's an empty string
        """
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")

    def test_state_id_attr(self):
        """
        Test that City has attribute state_id, and it's an empty string
        """
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_to_dict_creates_dict(self):
        """
        test to_dict method creates a dictionary with proper attrs
        """
        city = City()
        new_d = city.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in city.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """
        test that values in dict returned from to_dict are correct
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        city = City()
        new_d = city.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], city.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], city.updated_at.strftime(t_format))

    def test_str(self):
        """
        test that the str method has the correct output
        """
        city = City()
        string = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(string, str(city))
