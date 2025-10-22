from custlogger import get_custom_logger
import logging
def f1():
    logger = get_custom_logger(logging.DEBUG)
    logger.critical("It is critical message from test_1 module")
    logger.error("It is error message from test_1 module")
    logger.warning("It is warning message from test_1 module")
    logger.info("It is info message from test_1 module")
    logger.debug("It is debug message from test_1 module")
def f2():
    logger = get_custom_logger(logging.WARNING)
    logger.critical("It is critical message from test_1 module")
    logger.error("It is error message from test_1 module")
    logger.warning("It is warning message from test_1 module")
    logger.info("It is info message from test_1 module")
    logger.debug("It is debug message from test_1 module")
def f3():
    logger = get_custom_logger(logging.ERROR)
    logger.critical("It is critical message from test_1 module")
    logger.error("It is error message from test_1 module")
    logger.warning("It is warning message from test_1 module")
    logger.info("It is info message from test_1 module")
    logger.debug("It is debug message from test_1 module")
f1()
f2()
f3()