# -*- coding: utf-8 -*-
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from utils import locale_functions
from connectors import bikes_connector

import pystache

class StationBikesIntentHandler(AbstractRequestHandler):
    """Handler for Get New Question Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return is_intent_name("StationBikesIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        texts = locale_functions.get_locale_texts(handler_input)

        attr = handler_input.attributes_manager.session_attributes

        station_nr = handler_input.request_envelope.request.intent.slots.station_nr.value

        connector = bikes_connector.BikesConnector()
    
        response = connector.get_station_data(station_nr)

        if not response['error']:
            attr['station_nr'] = station_nr
            attr['info_requested'] = 'bikes'

            handler_input.attributes_manager.session_attributes = attr

            station_data = response['data']

            if station_data.status != 'OPEN':
                speech_text = pystache.render(texts.STATION_CLOSED_TEXT, {
                    'station_name': station_data.name,
                    'station_nr': station_data.number,
                })
            else:
                speech_text = pystache.render(texts.STATION_BIKES_TEXT, {
                    'station_name': station_data.name,
                    'station_nr': station_data.number,
                    'bikes_nr': station_data.available_bikes,
                })
        elif response['code'] == 404:
            speech_text = pystache.render(texts.STATION_NOT_FOUND_TEXT, {
                'station_nr': station_data.number,
            })
        else:
            speech_text = texts.STATION_GENERAL_ERROR_TEXT

        (handler_input.response_builder
                .speak(speech_text)
                .set_card(SimpleCard(texts.SKILL_NAME, speech_text)))

        return handler_input.response_builder.response