#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
import models
from models.city import City

class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete, delete_orphan"),
                            backref="state"

    @property
    def cities(self):
        """
        returns the list of City instances with state_id
        equals to the current State.id
        """
        from models import storage
        
        city_list = []
        cities = storage.all(City)

        for city in cities.value():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
