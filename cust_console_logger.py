#Write a program to define and use custom logger with both console and file handler
import logging
logger = logging.getLogger("Demologger")
logger.setLevel(logging.DEBUG)
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.ERROR)
fileHandler = logging.FileHandler("hi.log", mode="w")
fileHandler.setLevel(logging.DEBUG)
formater1 = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                              datefmt='%d/%m/%Y %I:%m:%S %p')
formater2 = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                              datefmt='%d/%m/%Y %I:%m:%S %p')
consoleHandler.setFormatter(formater1)
fileHandler.setFormatter(formater2)
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)
logger.critical("It is critical message")
logger.error('This is error message')
logger.warning("This is warning message")
logger.info("This is info message")
logger.debug("It is debug message")