"""
Module for review instances
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class for creating reviews which inherits
    `BaseModel` attributes
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
