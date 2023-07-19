#!/usr/bin/python3
"""
Module holds classess for storage engine for storing
data in to file and database.
"""
import json
from typing import Any


class FileStorage:
    """
    FileStorage():
        This class is the core storage engine for
        storing serialize JSON data to file and
        deserializes JSON data from file.
    """

    def __init__(self, path="") -> None:
        """
        __init__() -> None:
            path -> str:
                initializes instance of this class
                with parsed arg as properties.
        """
        self.__file_path = path
        self.__objects = {}

    @property
    def all(self) -> dict:
        """
        all() -> dict:
            Returns dictionary of all objects created
            with class_name and object id in the format
            <class name>.id>
            e.g: BaseModel.12121212.
        """
        return self.__objects

    @all.setter
    def all(self, obj={}):
        if type(obj) == dict:
            self.__objects = obj
        return self

    def new(self, obj):
        """
        new() -> None:
            creates an object in the __object with key
            of object's class name and id in the formart
            <obj class name>.id
            e.g: BaseModel.12121212.
        """
        self.__objects[obj.__class__
                       .__name__ + "." + obj.id] = obj.to_dict()

        return self

    def save(self):
        """
        save() -> None:
            serialized __objects to JSON format and write
            to file a directory/storage_file.json.
        """
        with open(self.__file_path, "w") as storage_file:
            storage_file.write(json.dumps(self.__objects))

        return self

    def reload(self) -> None:
        """
        reload() -> None:
            deserialized objects written to dictionary/storage_file.json
            to python dictionary and set it to __objects.
        """

        # checks if `self.__file_path` exist
        if len(self.__file_path) > 0:
            try:
                with open(self.__file_path) as storage_file:
                    json_data = storage_file.read()

                    # checks if `self.__file_path` content is a json string
                    if len(json_data) < 1 or json_data == "{}":
                        return
                    self.__objects = json.loads(json_data)
            except FileNotFoundError as err:
                return
