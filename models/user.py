#!/usr/bin/python3
"""User class module"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class that inherits from BaseModel

    Attributes:
        email (str): email empty string
        password (str): password empty string
        first_name (str): firstname empty string
        last_name: lastname empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
