import logging
from functools import cached_property


class ILoggable:
    @cached_property
    def logger(self):
        return logging.getLogger(self.__class__.__name__)
