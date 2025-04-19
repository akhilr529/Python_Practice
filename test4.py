#Write a program to define and use custom logger with different modules and with different log files?

import logging
import student2
logger = logging.getLogger("Test4logger")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler("test4.log",mode='w')
# fileHandler.setLevel(logging.ERROR)
formater = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",
                             datefmt="%d/%m/%Y %I:%M:%S %p")
fileHandler.setFormatter(formater)
logger.addHandler(fileHandler)
logger.critical("It is critical message from test4 module")
logger.error('This is error message from test4 module')
logger.warning("This is warning message from test4 module")
logger.info("This is info message from test4 module")
logger.debug("It is debug message from test4 module")