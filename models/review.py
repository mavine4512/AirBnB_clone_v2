#!/usr/bin/python3
"""
This function creates a Review class
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Creates a review clas with attributes such as:
    place, user, text
    """
    place_id = ""
    user_id = ""    
    text = ""

