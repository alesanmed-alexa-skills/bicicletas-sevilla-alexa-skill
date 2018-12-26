# coding: utf-8

import unittest

import test_contract
import test_contracts_api
import test_error
import test_station_position
import test_station
import test_stations_api

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromModule(test_contract))
    suite.addTests(loader.loadTestsFromModule(test_contracts_api))
    suite.addTests(loader.loadTestsFromModule(test_error))
    suite.addTests(loader.loadTestsFromModule(test_station_position))
    suite.addTests(loader.loadTestsFromModule(test_station))
    suite.addTests(loader.loadTestsFromModule(test_stations_api))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())