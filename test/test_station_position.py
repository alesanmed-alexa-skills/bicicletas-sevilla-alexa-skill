# coding: utf-8

"""
    JCDecaux API

    JCDecaux API for retrieving dynamic data about bike stations and contracts  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: alesanchezmedina@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))
import importlib

import unittest

from skill.connectors import bikes_api
from skill.connectors.bikes_api.models.station_position import StationPosition  # noqa: E501
from skill.connectors.bikes_api.rest import ApiException


class TestStationPosition(unittest.TestCase):
    """StationPosition unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStationPosition(self):
        """Test StationPosition"""
        StationPosition(
            lat=37.418732603824466,
            lng=-5.97319415962488
        )


if __name__ == '__main__':
    unittest.main()
