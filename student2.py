import logging
logger = logging.getLogger("Studentlogger")
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler("Student2.log", mode="w")
fileHandler.setLevel(logging.DEBUG)
formater = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s",
                             datefmt="%d/%m/%Y %I:%M:%S %p")
fileHandler.setFormatter(formater)
logger.addHandler(fileHandler)
logger.critical("It is critical message from student2 module")
logger.error('This is error message from student2 module')
logger.warning("This is warning message from student2 module")
logger.info("This is info message from student2 module")
logger.debug("It is debug message from student2 module")