import logging
logging.basicConfig(filename='mylog.txt', level=logging.DEBUG)
print("logging module demo")
logging.debug("this is debug message")
logging.warning("this is warning message")
logging.info("this is info message")
logging.error("this is error message")
logging.critical("this is critical message")