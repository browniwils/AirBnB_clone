"""
Module for User instances
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class for creating users which inherits
    `BaseModel` attributes
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
