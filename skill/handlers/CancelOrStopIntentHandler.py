# -*- coding: utf-8 -*-
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.ui import SimpleCard
from utils import locale_functions

class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        is_cancel_or_stop_intent = (is_intent_name("AMAZON.CancelIntent")(handler_input) or 
                                    is_intent_name("AMAZON.StopIntent")(handler_input))
        
        return is_cancel_or_stop_intent
                

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        texts = locale_functions.get_locale_texts(handler_input)

        (handler_input.response_builder
            .speak(texts.EXIT_TEXT)
            .set_card(SimpleCard(texts.SKILL_NAME, texts.EXIT_TEXT))
            .set_should_end_session(True))
        
        return handler_input.response_builder.response