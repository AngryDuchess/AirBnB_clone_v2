#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from models.city import City

db = os.getenv("HBNB_TYPE_STORAGE")

is_db = db == "db"


class State(*(BaseModel, Base) if is_db else (BaseModel,)):
    """ State class """

    if db == "db":
        from models.base_model import (Column,
                                       String, Integer, relationship)
        # Table Definition
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            """
            Implements the correct getting requirement for both
            FIleStorage
            """
            city_list = []
            objects = storage.all(City).values()
            for obj in objects:
                if obj.id == self.id:
                    city_list.append(id)
            return city_list
