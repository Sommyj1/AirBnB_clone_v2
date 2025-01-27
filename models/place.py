#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), 

nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # if getenv('HBNB_TYPE_STORAGE') == 'db':
    # reviews = relationship('Review', backref='place',
    #                        cascade='all, delete')
    # amenities = relationship('Amenity', secondary='place_amenity',

    #                          viewonly=False)

    # else:
    #     @property
    #     def reviews(self):
    #         """ Getter attribute reviews that returns the list of Review
    #         instances with place_id equals to the current Place.id """
    #         review_list = []
    #         for review in models.storage.all(Review).values():
    #             if review.place_id == self.id:
    #                 review_list.append(review)
    #         return review_list
