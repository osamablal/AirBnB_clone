#!/usr/bin/python3
"""Review class module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represents the review class

    Attributes:
        place_id (str): represents place's ID
        user_id (str): represents user's ID
        text (str): represents the review text
    """
    place_id = ""
    user_id = ""
    text = ""
