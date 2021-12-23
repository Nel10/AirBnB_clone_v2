#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        _tablename_ = "amenities"
        name = Column(String(128), nullable=False)
else:
    name = ""
