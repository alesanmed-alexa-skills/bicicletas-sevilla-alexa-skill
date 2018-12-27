# encoding: utf-8
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from pymongo import MongoClient
import urllib
from bson import ObjectId
from configurations import skill_config

_client = None

def __connect():
    username = urllib.parse.quote_plus(skill_config.DB_USER)
    password = urllib.parse.quote_plus(skill_config.DB_PASS)
    db_ip = urllib.parse.quote_plus(skill_config.DB_IP)
    db_port = urllib.parse.quote_plus(skill_config.DB_PORT)
    db_name = urllib.parse.quote_plus(skill_config.DB_NAME)

    global _client

    if not _client:
        _client = MongoClient('mongodb://%s:%s@%s:%s/%s' % 
                            (username, password, db_ip, db_port, db_name))

def get_station_name(station_nr):
    global _client
    
    station = _client[skill_config.DB_NAME].stations.find_one({
        'number': station_nr
    })

    return station