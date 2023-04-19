#!/usr/bin/python3
"""A database storage engine (DBStorage)"""
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
import os


class DBStorage:
    """define DBStorage class"""
    __engine = None
    __session = None
    __classes = [User, State, City, Amenity, Place, Review]

    def __init__(self):
        """a constructor for initializing new DBStorage instance"""
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      user, pwd, host, db), pool_pre_ping=True)

    if env == 'test':
        """drop all tables if environment variable HBNB_ENV is equal to test"""
        Base.metadata.drop_all()

    def all(self, cls=None):
        """method returns a dictionary of object"""
        my_dic = {}
        if cls in self.__session:
            result = self.__session.query(cls)
            for elemnt in result:
                key = "{}.{}".format(elemnt.__class__.__name__, elemnt.id)
                my_dic[key] = elemnt
        elif cls is None:
            for clss in self.__classes:
                result = self.__session.query(clss)
                for elemnt in result:
                    key = "{}.{}".format(elemnt.__class__.__name__, elemnt.id)
                    my_dic[key] = elemnt
        return my_dic

    def new(self, obj):
        """adds a new object to the current database"""
        self.__session.add(obj)

    def save(self):
        """saves chnages to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes obj from db"""
        self.__session.delete(obj)

    def reload(self):
        """creates all tables in the db & initializes new session"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """calls remove method"""
        self.__session.close()
