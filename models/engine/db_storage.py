#!/usr/bin/python3
"""
A module containing Database storage class for AirBnB console
"""
import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.user import User
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.base_model import Base
from sqlalchemy.orm.scoping import scoped_session

USER = os.getenv("HBNB_MYSQL_USER")
PASS = os.getenv("HBNB_MYSQL_PWD")
HOST = os.getenv("HBNB_MYSQL_HOST")
DBNAME = os.getenv("HBNB_MYSQL_DB")
current_process = os.getenv("HBNB_ENV")


class DBStorage:
    """
    Database storage class for AirBnB console
    """
    __engine = None
    __session = None
    classes = [State, City, Place, Amenity, User, Review]

    def __init__(self):
        """
        DBStorage class constructor
        """
        url = f"mysql+mysqldb://{USER}:{PASS}@{HOST}/{DBNAME}"
        self.__engine = create_engine(url, pool_pre_ping=True)
        if current_process == "test":
            try:
                Base.metadata.drop_all(self.__engine)
            except Exception as e:
                print("Error dropping tables: ", e)
        self.__Session = sessionmaker(self.__engine, expire_on_commit=False)

    def all(self, cls=None):
        """
        Returns all object in the session with type cls
        and all object is cls is None
        """
        session = self.__session
        formatted_objects = {}
        objects = []
        if cls is not None:
            objects = session.query(cls)
        else:
            for class_name in DBStorage.classes:
                objects.extend(session.query(class_name))
        for obj in objects:
            key = f"{obj.to_dict()['__class__']}.{obj.id}"
            formatted_objects.update({key: obj})
        return formatted_objects

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        if obj is not None:
            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """

        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        """
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(self.__Session)()

    def close(self):
        """deserializing the JSON file to objects"""
        self.__session.close()
