#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table(
    """the place amenity class"""
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False),
    Column(
        "amenity_id",
        String(60),
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
            cascade="all, delete-orphan")
        amenities = relationship(
            "Amenity",
            seconadry=place_amenity,
            viewonly=False)
    else:
        @property
        def review(self):
            m = []
            for id, rvw in models.storage.all(Review).items():
                if rvw.place.id == Review.id:
                    m.append(rvw)
            return m

        @property
        def amenities(self):
            los_angeles = []
            for angle in amenity_ids:
                if angel.id == set.id:
                    amenities_list.append(angel)
            return los_angeles

        @amenities.setter
        def amenities(self, angel):
            if type(angel) is Amenity:
                self.amenity_ids.append(angel)
