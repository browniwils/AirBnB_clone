"""
Module for State model
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class for creating state object which inherits
    `BaseModel` properties
    """
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiate State object
        """
        self.name = ""
        super().__init__(*args, **kwargs)
