import logging
logger = logging.getLogger("testlogger")
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("test.log", mode="a")

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.critical("It is critical message from test module")
logger.error("It is error message from test module")
logger.warning("It is warning message from test module")
logger.info("It is info message from test module")
logger.debug("It is debug message from test module")