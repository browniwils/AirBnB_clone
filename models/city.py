"""
Module for City instances
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Class for creating cities which inherits
    `BaseModel` attributes
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.state_id = ""
        self.name = ""