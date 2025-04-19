#Write a program to define and use custom logger with file handler?
import logging 
logger = logging.getLogger("Demologger")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler("custtest.log", mode="w")
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                              datefmt='%d/%m/%Y %I:%m:%S %p')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger.critical("It is critical message")
logger.error('This is error message')
logger.warning("This is warning message")
logger.info("This is info message")
logger.debug("It is debug message")