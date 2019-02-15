# encoding: utf-8
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from .db_object import DBObject

db = None

def get_db() -> DBObject:
    global db

    if db is None:
        db = DBObject()
    
    return db

