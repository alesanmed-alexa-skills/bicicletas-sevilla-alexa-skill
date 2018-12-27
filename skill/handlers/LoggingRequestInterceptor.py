# -*- coding: utf-8 -*-
from ask_sdk_core.dispatch_components import AbstractRequestInterceptor
from ask_sdk_model.ui import SimpleCard
from utils import logger

class LoggingRequestInterceptor(AbstractRequestInterceptor):
    def process(self, handler_input):
        attr = handler_input.attributes_manager.session_attributes
        intent_received = 'Unknown'

        logger.get_logger().info('Request: {}'.format(handler_input.request_envelope))

        if handler_input.request_envelope.request.object_type == 'IntentRequest':
            intent_received = handler_input.request_envelope.request.intent.name
        else:
            intent_received = handler_input.request_envelope.request.object_type

        logger.get_logger().info('Intent received: {}'.format(intent_received))
        logger.get_logger().info('User state: {}'.format(attr.get('state', None)))