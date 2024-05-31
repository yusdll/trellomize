# src/logger.py
import logging

# Logger class to handle logging functionality
class Logger:
    def __init__(self):
        self.logger = logging.getLogger("CodeManagementSystem")
        # set the logging level to DEBUG
        self.logger.setLevel(logging.DEBUG)
        # create a file handler to log messages to a file
        fh = logging.FileHandler("Code.log")
        fh.setLevel(logging.DEBUG)
        # create a stream handler to log messages to the console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # define the logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # set the formatter for both handlers
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    # Log a message with the specified level
    def log(self, message, level="info"):
        # check the log level and log the message accordingly
        if level == "debug":
            self.logger.debug(message)
        elif level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == "error":
            self.logger.error(message)
        elif level == "critical":
            self.logger.critical(message)
            