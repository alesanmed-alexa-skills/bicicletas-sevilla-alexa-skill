# encoding: utf-8
from __future__ import annotations
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from configurations import skill_config
import urllib
from pymongo import MongoClient, ASCENDING, DESCENDING
from utils import logger
from datetime import datetime


class DBObject():
    def __init__(self):        
        logger.get_logger().info('Connecting to database')

        self.username = urllib.parse.quote_plus(skill_config.DB_USER)
        self.password = urllib.parse.quote_plus(skill_config.DB_PASS)
        self.db_ip = urllib.parse.quote_plus(skill_config.DB_IP)
        self.db_port = urllib.parse.quote_plus(skill_config.DB_PORT)
        self.db_name = urllib.parse.quote_plus(skill_config.DB_NAME)

        self.client = MongoClient('mongodb://%s:%s@%s:%s/%s' %
                                  (self.username, self.password, self.db_ip, self.db_port, self.db_name))

    def user_exists(self, user_id: str) -> bool:
        db = self.client[self.db_name]

        res = db.users.count_documents({
            'user_id': user_id
        })

        return res == 1

    def insert_new_user(self, user_id: str) -> DBObject:
        db = self.client[self.db_name]

        db.users.insert_one({
            'user_id': user_id,
            'notification_date': datetime.now()
        })

        return self

    def notify_user(self, user_id: str) -> str:
        db = self.client[self.db_name]

        message = db.update_messages.find().sort('date', DESCENDING).limit(1)[0]

        db.users.find_one_and_update(
            {'user_id': user_id},
            {'$set': {'notification_date': datetime.now()}}
        )

        return message['message']
    
    def user_needs_notification(self, user_id: str) -> bool:
        db = self.client[self.db_name]

        user = db.users.find_one({ 'user_id': user_id })

        last_message = self.get_last_message()[0]

        print(user['notification_date'])

        return user['notification_date'] < last_message['date']

    def get_last_message(self) -> object:
        db = self.client[self.db_name]

        message = db.update_messages.find().sort('date', DESCENDING).limit(1)

        return message

    def get_station_name(self, station_nr: str) -> str:
        db = self.client[self.db_name]

        name = db.stations.find_one({ 'number': station_nr })['name'].title()

        return name