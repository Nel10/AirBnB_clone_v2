#!/usr/bin/python3
"""
New engine DBStorage
"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.exc import InvalidRequestError

classes = {"User": User, "State": State, "City": City, "Amenity": Amenity,
           "Place": Place, "Review": Review}


class DBStorage:
    """Representation of DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = ('HBNB_MYSQL_PWD')
        host = ('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        port = 3306
        cone = ('mysql+mysqldb://{}:{}@{}/{}'.format(user, password, host,
                                                     port, database, pol,
                                                     pool_pre_ping=True))
        self.__engine = create_engine(cone)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        if not cls:
            for key, val in classes.items():
                try:
                    objects = self.__session.query(value).all()
                    for obj in objects:
                        objc_key = obj.__class__.__name__ + '.' + obj.id
                        self.__objects[objc_key] = obj
                except InvalidRequestError:
                    pass
            return self.__objects
        else:
            cls = classes[cls]
            objects = self.__session.query(cls).all()
            for obj in objects:
                objc_key = obj.__class__.__name__ + '.' + obj.id
                self.__objects[objc_key] = obj
            return self.__objects

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        scop = scoped_session(session_factory)
        self.__session = scop()
