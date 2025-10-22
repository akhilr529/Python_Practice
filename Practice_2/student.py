import logging
logger = logging.getLogger("studentlogger")
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler("student.log", mode="a")
fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)

logger.critical("It is critical message from student module")
logger.error("It is error message from student module")
logger.warning("It is warning message from student module")
logger.info("It is info message from student module")
logger.debug("It is debug message from student module")