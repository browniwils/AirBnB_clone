"""
Module for Amenity model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class for creating amenities objects which inherits
    `BaseModel` properties
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiate Amenity object
        """
        self.name = ""
        super().__init__(*args, **kwargs)
