#!/usr/bin/python3
"""
Module is paprent class for objects in the airbnb project
"""
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """
    BaseModel is the parent class that other
    classess will inherit its properties
    """
    def __init__(self, *args, **kwargs):
        """
        Instantiate BaseModel object
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        try:
                            setattr(self, key, datetime.fromisoformat(val))
                        except ValueError as err:
                            pass
                    else:
                        setattr(self, key, val)

        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self) -> str:
        """
        Return or prints string representation
        of this object
        """
        name = self.__class__.__name__
        id = self.id
        dictionary = self.__dict__
        return "[{}] ({}) {}".format(name, id, dictionary)

    def save(self):
        """
        Updates this object and save to storage
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self) -> dict:
        """
        Returns object in dictionary in addition with
        object's class name as `__class__` as a key
        and `class name` as value
        """
        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
