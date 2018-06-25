import logging
import inspect


class LogHelper:

    @classmethod
    def logger(cls) -> logging:
        stack = inspect.stack()
        the_class = stack[1][0].f_locals["self"].__class__
        return logging.getLogger(str(the_class))
