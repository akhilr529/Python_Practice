import logging
from custlogger import get_custom_logger
def logstudent():
    logger = get_custom_logger(logging.WARNING)
    logger.critical("Critical message from student3 module")
    logger.error("Error message from student3 module")
    logger.warning("Warning message from student3 module")
    logger.info("info message from student3 module")
    logger.debug("debug message from student3 module")
logstudent()