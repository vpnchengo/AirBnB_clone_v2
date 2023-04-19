#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
    If environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
    instantiates DBStorage
    else, instatiates FileStorage
"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from os import getenv


if os.getenv('HBNB_TYPE_STORAGE') = 'db':
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
