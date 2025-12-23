from xml.etree.ElementTree import ParseError
from logs.logger import *


def error_handler(fn):
    def wrapper(path):
        try:
            return fn(path)
        except (ValueError, FileNotFoundError, TypeError, ParseError) as error:
            log_event(error)
            return error

    return wrapper
