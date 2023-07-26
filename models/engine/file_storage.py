#!/usr/bin/python3
"""
Module is a class for storage engine for storing
data in to file and database.
"""
import json
from utils import prep_save_to_file


class FileStorage:
    """
    Storage object class is the core storage engine for
    storing serialize JSON data to file and
    deserializes JSON data from file.
    """
    __file_path = "file.json"
    __objects = {}
    def __init__(self, path=""):
        """
        Instanciate storage object.
        """
        self.__file_path = path
        self.__objects = {}

    def all(self):
        """
        Returns all storage objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Creates new storage object.
        `obj` is model object.
        """
        id = obj.id
        name = obj.__class__.__name__
        self.__objects["{}.{}".format(name, id)] = obj.to_dict()
        return self

    def save(self):
        """
        Save serialized storage objects to JSON data,
        and write it to file in a .json extension.
        """
        prep_save_to_file(self.__objects)          

        with open(self.__file_path, "w") as storage_file:
            storage_file.write(json.dumps(self.__objects))
        
        prep_save_to_file(self.__objects, "end")
        return self

    def reload(self):
        """
        Loads JSON data from file with .json extension,
        and deserialized it to storage objects.
        """

        # checks if `self.__file_path` exist
        if len(self.__file_path) > 0:
            try:
                with open(self.__file_path) as storage_file:
                    json_data = storage_file.read()

                    # checks if self.__file_path content is empty
                    if len(json_data) < 1 or json_data == "{}":
                        return
                    self.__objects = json.loads(json_data)
            except FileNotFoundError as err:
                return
