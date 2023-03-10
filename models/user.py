#!/usr/bin/python3
"""Defines the class User"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user

    Attributes:
    email (str): The email of the user
    password (str): The password of the user
    first_name (str): The firstname of the suer
    last_name (str): The lastname  of the user
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
