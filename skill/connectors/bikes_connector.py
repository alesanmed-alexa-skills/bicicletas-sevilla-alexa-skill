# encoding: utf-8
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from . import bikes_api
from .bikes_api.rest import ApiException
from configurations import skill_config
from utils import logger

class BikesConnector():
    def __init__(self):
        api_config = bikes_api.Configuration()
        api_config.api_key['apiKey'] = skill_config.JCDECAUX_KEY

        self.api = bikes_api.StationsApi(
                bikes_api.ApiClient(configuration=api_config)
            )  # noqa: E501

    def get_station_data(self, station_nr, contract='Seville'):
        response = {}
        try:
            response = {
                'error': False,
                'data': self.api.stations_station_number_get(station_nr, contract)
            }
        except ApiException as e:
            logger.get_logger().error('BikesConnector -> get_station_data error: {}'.format(e))
            response = {
                'error': True,
                'code': int(e.status)
            }
        
        return response