"""
Module for City model
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class for creating city object which inherits
    `BaseModel` properties
    """
    def __init__(self, *args, **kwargs) -> None:
        """
        Instantiate City object
        """
        self.state_id = ""
        self.name = ""
        super().__init__(*args, **kwargs)
