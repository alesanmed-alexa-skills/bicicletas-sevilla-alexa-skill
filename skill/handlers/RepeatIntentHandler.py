# -*- coding: utf-8 -*-
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

import pystache
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from utils import locale_functions
from connectors import bikes_connector

class RepeatIntentHandler(AbstractRequestHandler):
    """Handler for Repeat Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("AMAZON.RepeatIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        texts = locale_functions.get_locale_texts(handler_input)
        
        attr = handler_input.attributes_manager.session_attributes

        connector = bikes_connector.BikesConnector()

        if attr['station_nr']:
            station_data = connector.get_station_data(attr['station_nr'])
            info_requested = attr['info_requested']

            speech_text = None

            if station_data.status == 'OPEN':
                if info_requested == 'bikes':
                    speech_text = pystache.render(texts.STATION_BIKES_TEXT, {
                        'station_name': station_data.name,
                        'station_nr': station_data.number,
                        'bikes_nr': station_data.available_bikes,
                    })
                elif info_requested == 'slots':
                    speech_text = pystache.render(texts.STATION_BIKES_TEXT, {
                        'station_name': station_data.name,
                        'station_nr': station_data.number,
                        'slots_nr': station_data.bike_stands,
                    })
                elif info_requested == 'status':
                    speech_text = pystache.render(texts.STATION_STATUS_TEXT, {
                        'station_name': station_data.name,
                        'station_nr': station_data.number,
                        'bikes_nr': station_data.available_bikes,
                        'slots_nr': station_data.bike_stands,
                    })
            else:
                speech_text = pystache.render(texts.STATION_CLOSED_TEXT, {
                    'station_name': station_data.name,
                    'station_nr': station_data.number,
                })

            (handler_input.response_builder
                        .speak(speech_text)
                        .set_card(SimpleCard(texts.SKILL_NAME, speech_text)))
        else:
            (handler_input
                .response_builder
                .speak(texts.HELLO_TEXT)
                .set_card(SimpleCard(texts.SKILL_NAME, texts.HELLO_TEXT))
                .ask(texts.HELLO_REPROMPT_TEXT))

        return handler_input.response_builder.response