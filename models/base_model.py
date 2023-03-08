#!/usr/bin/python3
"""Defines the BaseModel for the Airbnb console"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """basemodel that defines all common attributes for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialize the BaseModel class
        Attributes:
        Args:
            *args (any): inputted arguments
            **kwargs (dict): Key/value pairs of inputted arguments
        id (str) - assign with an uuid when an instance is created.
        created_at (time): datetime - assign with the current datetime when
            an instance is created
        updated_at (time): datetime - assign with the current datetime when
            n instance is created and it will be updated every time you
            change your object.
        """
        timeform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, timeform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        """Updates the updated_at attribute with the current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the __dict__ of the instance.
        Return:
            dictonary (dict): Dictionary object that contains __dict__
        """
        returndict = self.__dict__.copy()
        returndict["created_at"] = self.created_at.isoformat()
        returndict["updated_at"] = self.updated_at.isoformat()
        returndict["__class__"] = self.__class__.__name__
        return returndict

    def __str__(self):
        """str representation of the BaseModel class
        Return:
            string(str): string descriptor for the BaseModel Class
        """
        classname = self.__class__.__name__
        return "[{}] ({}) {}".format(classname, self.id, self.__dict__)
