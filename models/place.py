#!/usr/bin/python3
"""
This function creates a place class
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String, Integer, Float, Table, ForeignKey
from sqlalchemy.orm import relationship

if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                         Column('place_id',
                                String(60),
                                ForeignKey('places.id'),
                                primary_key=True,
                                nullable=False),
                          Column('amenity_id',
                                  String(60),
                                  ForeignKey('amenities.id'),
                                  primary_key=True,
                                  nullable=False))


class Place(BaseModel, Base):
    """
    Creates a class for place that has different attributes:
    strings and integers
    """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'place'
        city_id = Column(String(60),
                        ForeignKey("cities.id"),
                        nullable=False)
        user_id = Column(String(60),
                         ForeignKey("users.id"),
                         nullable=False)
        name = Column(String(128),
                         nullable=False)
        description = Column(String(1024),
                      nullable=True)
        number_rooms = Column(Integer,
                              default=0,
                              nullable=False)
        number_bathrooms = Column(Integer,
                              default=0,
                              nullable=False)
        max_guest = Column(Integer,
                           default=0,
                           nullable=False)
        price_by_night = Column(Integer,
                           default=0,
                           nullable=False)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Reviews", cascade="all, delete",
                                backref="places")
        amenities = relationship("Amenity",
                                secondary='place_amenity',
                                viewonly=False,
                                backref="places_amenities")
    else:
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

    def __init__(self, *args, **kwargs):
        """Initialize the place"""
        super().__init__(*args, **kwargs)

    @property
    def reviews(self):
        """Attribute that returns list of reviews instances"""
        values_review = []
        for review in values_review:
            if review.place_id == self.id:
                list_review.append(review)
        return list_review

    if getenv(HBNB_TYPE_STRONG) != 'db':
       @property
       def amenities(self):
            """Attribute that returns list of Amenity instances"""
           values_amenity = models.strong.all("Amenity").values()
           list_amenity = []
           for amenity in values_amenity:
                if amenity.place_id == self.id:
                    list_amenity.append(amenity)
           return list_amenity
