import logging
from custlogger import get_custom_logger
def f1():
    logger = get_custom_logger(logging.WARNING)
    logger.critical("Critical message from f1")
    logger.error("Error message from f1")
    logger.warning("Warning message from f1")
    logger.info("info message from f1")
    logger.debug("debug message from f1")

def f2():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical("Critical message from f2")
    logger.error("Error message from f2")
    logger.warning("Warning message from f2")
    logger.info("info message from f2")
    logger.debug("debug message from f2")

f1()
f2()
