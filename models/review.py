"""
Module for review model
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for creating review object which inherits
    `BaseModel` properties
    """
    place_id = ""
    user_id = ""
    text = ""
    def __init__(self, *args, **kwargs):
        """
        Instantiate Review object
        """
        self.place_id = ""
        self.user_id = ""
        self.text = ""
        super().__init__(*args, **kwargs)
