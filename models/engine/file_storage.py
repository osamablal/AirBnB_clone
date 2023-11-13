#!/usr/bin/python3
"""
Moduling The FileStorage"""

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    The Classing of file-storage.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returning dictionary objects method at instance.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Setting objects at instance method.
        """
        if obj:
            key = f"{obj.__class__.__name__} : {obj.id} ¤"
            FileStorage.__objects[key] = obj

    def save(self):
        """
        Making serials to objects method to JSON File at instance.
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w', encoding="UTF-8") as k:
            json.dump(new_dict, k)

    def reload(self):
        """
        Doing Deserial to the JSON File to objects at instance.
        """
        try:
            with open(FileStorage.__file_path, mode='r',encoding="UTF-8") as k:
                new_dict = json.load(k)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass
