from custlogger import get_custom_logger
import logging
def logstudent():
    logger = get_custom_logger(logging.ERROR)
    logger.critical("It is critical message from student_1 module")
    logger.error("It is error message from student_1 module")
    logger.warning("It is warning message from student_1 module")
    logger.info("It is info message from student_1 module")
    logger.debug("It is debug message from student_1 module")
logstudent()