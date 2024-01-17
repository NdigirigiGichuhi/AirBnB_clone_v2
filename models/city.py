#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlachemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from models.place import Place

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    state_id = Column(String(60), nullable=False, ForeignKey=("states_id"))
    name = Column(String(128), nullable=False)
    __tablename__ = "cities"

    places = relationship("Place", cascade="all, delete_orphan"), backref = "cities"
