#Creation of generi logger and usage
import inspect
import logging
def get_custom_logger(level):
    function_name = inspect.stack()[1][3]
    logger_name = function_name + "logger"
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    fileHandler = logging.FileHandler("{}.log".format(function_name), mode="a")
    # fileHandler = logging.FileHandler("mixed.log",mode="a")
    fileHandler.setLevel(level)
    formater = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s',
                                 datefmt='%d/%m/%Y %I:%m:%S %p')
    fileHandler.setFormatter(formater)
    logger.addHandler(fileHandler)
    return logger