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

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        texts = locale_functions.get_locale_texts(handler_input)
        
        (handler_input
            .response_builder
            .speak(texts.HELLO_TEXT)
            .set_card(SimpleCard(texts.SKILL_NAME, texts.HELLO_TEXT))
            .ask(texts.HELLO_REPROMPT_TEXT))
        
        return handler_input.response_builder.response