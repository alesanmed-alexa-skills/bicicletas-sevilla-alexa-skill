# -*- coding: utf-8 -*-
from sys import path
import os
from os.path import dirname as dir

path.append(dir(path[0]))
import importlib

def get_locale_texts(handler_input):
  return importlib.import_module('i18n.{}'.format(
          __transform_locale(handler_input.request_envelope.request.locale)))

def __transform_locale(locale):
  return locale.replace('-', '_')