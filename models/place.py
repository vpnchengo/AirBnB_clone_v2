#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table("place_amenity", Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(
        String(60),
        ForeignKey("users.id"),
        nullable=False)
    user_id = Column(
        String(60),
        ForeignKey("users.id"),
        nullable=False)
    name = Column(
        String(128),
        nullable=False)
    description = Column(
        String(1024),
        nullable=True)
    number_rooms = Column(
        Integer,
        default=0,
        nullable=False)
    number_bathrooms = Column(
        Integer,
        default=0,
        nullable=False)
    max_guest = Column(
        Integer,
        default=0,
        nullable=False)
    price_by_night = Column(
        Integer,
        default=0,
        nullable=False)
    latitude = Column(
        Float,
        nullable=True)
    longitude = Column(
        Float,
        nullable=True)
    amenity_ids = []
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete, delete-orphan")
        amenities = relationship(
            "Amenity",
            seconadry=place_amenity,
            viewonly=False)
    else:
        @property
        def review(self):
            """Getter attribute reviews that returns the list of Review
            instances with place_id equals to the current Place.id
            """
            my_list = []
            results = models.storage.all('Review').items()
            for review in results:
                if self.id == review.place.id:
                    my_list.append(review)
            return my_list

        @property
        def amenities(self):
            """getter attribute"""
            my_list = []
            results = models.storage.all('Amenity').values()
            for amenity in results:
                if self.id == amenity.amenity_ids:
                    my_list.append(amenity)
            return my_list

        @amenities.setter
        def amenities(self, value):
            """ setter attribute"""
            if isinstance(obj, 'Amenity'):
                self.amenity_ids.append(obj.id)
