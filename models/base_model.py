#!/usr/bin/python3
"""
The Moduling of BaseModel.
"""

import uuid
from datetime import datetime
import models


class BaseModel():
    """
    The Class of base_model.
    """

    def __init__(self, **kwargs):
        """
        class constructor for class BaseModel
        """
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')

            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        The String of base_model at instanc.
        """
        return f"[{self.__class__.__name__}] and ({self.id}) : {self.__dict__} ¤"

    def save(self):
        """
        Updating a new current date time.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Moduling dictionary instance """
        new_dict = dict(self.__dict__)
        new_dict['created_at'] = self.__dict__['created_at'].isoformat()
        new_dict['updated_at'] = self.__dict__['updated_at'].isoformat()
        new_dict['__class__'] = self.__class__.__name__
        return new_dict
