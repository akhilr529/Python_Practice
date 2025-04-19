from custlogger import get_custom_logger
import logging
def logtest():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical("Critical message from test6 module")
    logger.error("Error message from test6 module")
    logger.warning("Warning message from test6 module")
    logger.info("info message from test6 module")
    logger.debug("debug message from test6 module")

logtest()