#!/usr/bin/python3
"""Place class module"""
from models.base_model import BaseModel


class Place(BaseModel):
    """represents the location

    Attributes:
        city_id (str): represents the id of the street
        user_id (str): represents the id of the user
        name (str): represents the place's name
        description (str): represents the place's description
        number_rooms (int): number of rooms
        number_bathrooms (int): number of bathrooms
        max_guest (int): max guest per place
        price_by_night (int): represents the price for a single night
        latitude (float): coordinate position x
        longitude (float): coordinate position y
        amenity_ids (list): list all the associated Amenity
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
