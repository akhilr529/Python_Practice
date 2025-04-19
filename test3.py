import logging

logging.basicConfig(filename="test.log", level=logging.DEBUG)
import student
logging.critical("critical message by test module")
logging.error("error message by test module")
logging.warning("warning message by test module")
logging.info("info message by test module")
logging.debug("debug message by test module")