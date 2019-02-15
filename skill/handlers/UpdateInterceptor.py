# -*- coding: utf-8 -*-
from ask_sdk_core.dispatch_components import AbstractRequestInterceptor
from ask_sdk_model.ui import SimpleCard
from utils import logger
from connectors import db_utils

class UpdateInterceptor(AbstractRequestInterceptor):
    def process(self, handler_input):
        logger.get_logger().info("UpdateInterceptor - storing user...")

        req_envelope = handler_input.request_envelope

        user_id = req_envelope.context.system.user.user_id

        db = db_utils.get_db()
        
        if not db.user_exists(user_id):
            db.insert_new_user(user_id)