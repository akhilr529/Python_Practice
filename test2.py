import logging
logging.basicConfig(filename="abc.log", level= logging.DEBUG, filemode='w')
logging.basicConfig(filename="xyz", level= logging.ERROR, filemode='w')
logging.critical("It is critical message")
logging.error('This is error message')
logging.warning("This is warning message")
logging.info("This is info message")
logging.debug("It is debug message")