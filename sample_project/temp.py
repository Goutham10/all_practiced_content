import logging
from unittest import result
import employee


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s:')

file_handler = logging.FileHandler('test.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()

logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    try:
        result =  x/y
    except ZeroDivisionError:
        logger.exception("tried to divide by zero")
    else:
        return result


addition = add(20, 40)
logger.debug("add : {} ".format(addition))

subtraction = sub(22, 44)
logger.debug("sub : {} ".format(subtraction))

division = div(22, 2)
logger.debug("div : {} ".format(division))