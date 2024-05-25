# src/logger.py
import logging

class Logger:
    def __init__(self):
        self.logger = logging.getLogger("CodeManagementSystem")
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler("Code.log")
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)