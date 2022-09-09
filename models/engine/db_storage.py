#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker


class DBStorage:
    """a database storage engine"""
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{]".format(
            getenv("HBNB_MYSQL_USER"), getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"), getenv("HBNB_MYSQL_DB"),
            pool_pre_ping=True))
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
    """query on the current database session (self.__session)
    all objects depending of the class name (argument cls)"""
    Base.metadata.create_all(self.__engine)
    self.__session = Session(self.__engine)

        if cls:
            cls = eval(cls.__name__)
            my_query = self.__session.query(cls).all()
        else:
            my_objs = [User, Place, Review, City, State, Amenity]
            my_query = []
            for elem in my_objs:
                my_query.extend(self.__session.query(elem)).all()

        object_dict = dict()
        for obj in my_query:
            object_dict[f"{type(obj).__name__}.{obj.id}"] = obj

        return object_dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database & the current database session"""
        Base.metadata.create_all(self.__engine)
        sessio = sessionmaker(binds=self.__engine,
                            expire_on_commit=False)
        self.__session = scoped_session(sessio)
