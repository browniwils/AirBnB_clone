#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
from models import storage
"""
Module serves base classess for objects
in the airbnb project
"""


class BaseModel:
    """
    BaseModel is the base class that other
    class will be inherited from
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Initializes objects when instance is
        created
        """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.fromisoformat(val))
                    else:
                        setattr(self, key, val)

        if len(kwargs) == 0:
            storage.new(self)

    def __str__(self) -> str:
        """
        Return and prints string representation
        of the class model
        """
        name = self.__class__.__name__
        id = self.id
        diction = self.__dict__
        return "[{}] ({}) {}".format(name, id, diction)

    def save(self) -> None:
        """
        Method updates object's updated field
        with current date stamp
        """
        self.updated_at = datetime.now()
        self.updated_at = self.updated_at.isoformat()
        storage.save()

    def to_dict(self) -> dict:
        """
        to_dict -> returns a python dictionary
        containing all keys and values pairs of
        __dict__ the instance with __class__ key
        and classname value
        """

        dictionary = self.__dict__
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
