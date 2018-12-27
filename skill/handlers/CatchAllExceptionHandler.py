# -*- coding: utf-8 -*-
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_model.ui import SimpleCard
from utils import logger, locale_functions

class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Catch all exception handler, log exception and
    respond with custom message.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.get_logger().error(exception, exc_info=True)

        texts = locale_functions.get_locale_texts(handler_input)

        (handler_input.response_builder
            .speak(texts.EXCEPTION_TEXT)
            .set_card(SimpleCard(texts.SKILL_NAME, texts.EXCEPTION_TEXT))
            .ask(texts.EXCEPTION_REPROMPT_TEXT))

        return handler_input.response_builder.response