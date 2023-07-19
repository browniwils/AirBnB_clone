"""
Module for State instances
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class for creating states which inherits
    `BaseModel` attributes
    """
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = ""