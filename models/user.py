#!/usr/bin/python3
"""
This function creates a User class
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """
    Creates a User class with attributes
    email, password, first_name, last_name
    """
    email = ""
    password = ""    
    first_name = ""
    last_name = ""

