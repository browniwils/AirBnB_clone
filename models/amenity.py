"""
Module for Amenity model
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class for creating amenities objects which inherits
    `BaseModel` properties
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Instantiate Amenity object
        """
        self.name = ""
        super().__init__(*args, **kwargs)
