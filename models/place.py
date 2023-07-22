"""
Module for place model
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class for creating place object which inherits
    `BaseModel` properties
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Instantiate Place object
        """
        self.city_id = ""
        self.user_id = ""
        self.name = ""
        self.description = ""
        self.number_rooms = 0
        self.number_bathrooms = 0
        self.max_guest = 0
        self.price_by_night = 0
        self.latitude = 0.0
        self.longitude = 0.0
        self.amenity_ids = []
        super().__init__(*args, **kwargs)
