#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Foreignkey, Integer


class City(BaseModel,Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60),
            Foreignkey("states.id", ondelete="CASCADE"),
            nullable=false)
    places = relationship('Place", backref=citiess", cascade=all, delete")
