import logging
import logging.config
logging.config.fileConfig("logging_config.init")
logger = logging.getLogger("demologger")
logger.critical("It is critical message")
logger.error('This is error message')
logger.warning("This is warning message")
logger.info("This is info message")
logger.debug("It is debug message")