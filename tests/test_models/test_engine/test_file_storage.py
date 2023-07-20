#!/usr/bin/python3
""" Test module for testing Filestorage class """
from os import path
from models import storage
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os, unittest


class test_storage(unittest.TestCase):
    """ Main testing class """
    storage_path = "database/storage_db.json"
    def setUp(self):
        """ Test setup """
        try:
            os.remove(self.storage_path)
        except Exception:
            pass
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """ Test shutdown """
        try:
            os.remove(self.storage_path)
        except Exception:
            pass

    def test_no_objs(self):
        """ Test for storage objects holders """
        self.assertEqual(storage.all, {})

    def test_all(self):
        """ Test for storage `all` attribute """
        storage = FileStorage()
        storage_objects = storage.all()
        self.assertIsNotNone(storage_objects)
        self.assertEqual(type(storage_objects), dict)
        self.assertIs(storage_objects, storage._FileStorage__objects)

    def test_save_create(self):
        """ Test for saving object with models  """
        base_model = BaseModel()
        base_model_key = "{}.{}".format('BaseModel', base_model.id)
        user_model = User()
        user_model_key = "{}.{}".format('User', user_model.id)
        city_model = City()
        city_model_key = "{}.{}".format('City', city_model.id)
        amenity_model = Amenity()
        amenity_model_key = "{}.{}".format('Amenity', amenity_model.id)
        place_model = Place()
        place_model_key = "{}.{}".format('Place', place_model.id)
        review_model = Review()
        review_model_key = "{}.{}".format('Review', review_model.id)
        state_model = State()
        state_model_key = "{}.{}".format('State', state_model.id)

        self.assertEqual(base_model, storage.all[base_model_key])
        self.assertEqual(user_model, storage.all[user_model_key])
        self.assertEqual(city_model, storage.all[city_model_key])
        self.assertEqual(amenity_model, storage.all[amenity_model_key])
        self.assertEqual(place_model, storage.all[place_model_key])
        self.assertEqual(review_model, storage.all[review_model_key])
        self.assertEqual(state_model, storage.all[state_model_key])

    def test_create_new_object_storage(self):
        """ Test for creating new object in storage class """
        with self.assertRaises(TypeError):
            storage.new()

    def test_new_objects(self):
        """ Test for creating new model objects """
        base_model = BaseModel(id='123')
        base_model_key = "{}.{}".format('BaseModel', base_model.id)
        user_model = User(id='01')
        user_model_key = "{}.{}".format('User', user_model.id)
        city_model = City(id='02')
        city_model_key = "{}.{}".format('City', city_model.id)
        amenity_model = Amenity(id='03')
        amenity_model_key = "{}.{}".format('Amenity', amenity_model.id)
        place_model = Place(id='04')
        place_model_key = "{}.{}".format('Place', place_model.id)
        review_model = Review(id='05')
        review_model_key = "{}.{}".format('Review', review_model.id)
        state_model = State(id='06')
        state_model_key = "{}.{}".format('State', state_model.id)

        self.assertEqual(storage.all, {})
        base_model.id = 123
        storage.new(base_model)
        storage.new(user_model)
        storage.new(city_model)
        storage.new(amenity_model)
        storage.new(place_model)
        storage.new(review_model)
        storage.new(state_model)
        self.assertEqual(base_model, storage.all[base_model_key])
        self.assertEqual(user_model, storage.all[user_model_key])
        self.assertEqual(city_model, storage.all[city_model_key])
        self.assertEqual(amenity_model, storage.all[amenity_model_key])
        self.assertEqual(place_model, storage.all[place_model_key])
        self.assertEqual(review_model, storage.all[review_model_key])
        self.assertEqual(state_model, storage.all[state_model_key])

    def test_reload(self):
        """ Test for reloading objects in storage class """
        base_model = BaseModel()
        user_model = User()
        city_model = City()
        amenity_model = Amenity()
        place_model = Place()
        review_model = Review()
        state_model = State()
        base_model_key = "{}.{}".format('BaseModel', base_model.id)
        user_model_key = "{}.{}".format('User', user_model.id)
        city_model_key = "{}.{}".format('City', city_model.id)
        amenity_model_key = "{}.{}".format('Amenity', amenity_model.id)
        place_model_key = "{}.{}".format('Place', place_model.id)
        review_model_key = "{}.{}".format('Review', review_model.id)
        state_model_key = "{}.{}".format('State', state_model.id)
        storage.save()

        self.assertTrue(path.isfile(self.storage_path))
        FileStorage._FileStorage__objects = {}
        storage.reload()

        self.assertTrue(base_model_key in storage.all.keys())
        self.assertEqual(base_model.id, storage.all[base_model_key].id)
        
        self.assertTrue(user_model_key in storage.all.keys())
        self.assertEqual(user_model.id, storage.all[user_model_key].id)

        self.assertTrue(city_model_key in storage.all.keys())
        self.assertEqual(city_model.id, storage.all[city_model_key].id)

        self.assertTrue(amenity_model_key in storage.all.keys())
        self.assertEqual(amenity_model.id, storage.all[amenity_model_key].id)

        self.assertTrue(place_model_key in storage.all.keys())
        self.assertEqual(place_model.id, storage.all[place_model_key].id)

        self.assertTrue(review_model_key in storage.all.keys())
        self.assertEqual(review_model.id, storage.all[review_model_key].id)

        self.assertTrue(state_model_key in storage.all.keys())
        self.assertEqual(state_model.id, storage.all[state_model_key].id)