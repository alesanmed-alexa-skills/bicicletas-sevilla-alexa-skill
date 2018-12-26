# -*- coding: utf-8 -*-
import os
from importlib import import_module
import inspect

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.dispatch_components import AbstractRequestInterceptor
from ask_sdk_core.dispatch_components import AbstractRequestHandler

from utils import logger


logger.init_logger()

sb = SkillBuilder()

logger.get_logger().info('SkillBuilder created')

base_path = os.path.join(os.path.dirname(__file__), 'handlers')
files = os.listdir(base_path)

for file_name in files:
    handler, _ = os.path.splitext(file_name)

    HandlerClass = getattr(import_module('handlers.{}'.format(handler)), handler)
    handler_parent_classes = inspect.getmro(HandlerClass)

    logger.get_logger().info('Adding {} to SkillBuilder'.format(handler))

    if AbstractRequestHandler in handler_parent_classes:
        sb.add_request_handler(HandlerClass())
    elif AbstractExceptionHandler in handler_parent_classes:
        sb.add_exception_handler(HandlerClass())
    elif AbstractRequestInterceptor in handler_parent_classes:
        sb.add_global_request_interceptor(HandlerClass())

logger.get_logger().info('Added all handlers to SkillBuilder')

handler = sb.lambda_handler()