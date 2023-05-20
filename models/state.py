#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
import models.city import City
import os


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances
        with state_id equals to the current State.id =>
        It will be the FileStorage relationship between State and City
        """
        mylist = []
        extracted_result = models.storage.all(City).values()
        for city in extracted_result:
            if self.id == city.state_id:
                mylist.append(city)
        return mylist
