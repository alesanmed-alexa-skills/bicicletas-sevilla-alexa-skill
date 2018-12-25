# encoding: utf-8
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from pymongo import MongoClient
import urllib
from bson import ObjectId
from configurations import skill_config

class SkillDatabase():
    def __init__(self):
        self.DB_IP = skill_config.DB_IP
        self.DB_PORT = skill_config.DB_PORT
        self.DB_NAME = skill_config.DB_NAME
        self.DB_USER = skill_config.DB_USER
        self.DB_PASS = skill_config.DB_PASS
        
        self.client = self.__connect()

    def __connect(self):
        username = urllib.parse.quote_plus(self.DB_USER)
        password = urllib.parse.quote_plus(self.DB_PASS)
        db_ip = urllib.parse.quote_plus(self.DB_IP)
        db_port = urllib.parse.quote_plus(self.DB_PORT)
        db_name = urllib.parse.quote_plus(self.DB_NAME)

        client = MongoClient('mongodb://%s:%s@%s:%s/%s' % 
                            (username, password, db_ip, db_port, db_name))

        return client