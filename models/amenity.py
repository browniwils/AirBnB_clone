"""
Module for Amenity instances
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class for creating amenities which inherits
    `BaseModel` attributes
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = ""