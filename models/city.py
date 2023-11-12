#!/usr/bin/python3
"""
Making a class that inherent the base model.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    The city classing.
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """
        Configuares the city.
        """
        BaseModel.__init__(self, *args, **kwargs)

