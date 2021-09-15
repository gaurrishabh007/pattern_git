import logging
logging.basicConfig(filename='log.txt', level=logging.WARNING)
print("logging module demo")
logging.debug("this is debug message")
logging.info("this is info message")
logging.warning("this is warning message")
logging.error("this is error message")
logging.critical("this is critical message")