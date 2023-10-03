"""
Module for User model
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class for creating user object which inherits
    `BaseModel` properties
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        Instantiate User object
        """
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
        super().__init__(*args, **kwargs)
