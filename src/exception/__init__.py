import sys
from src.logging import logging

class DLClassifierException(Exception):
    def __init__(self, error_message, error_details:sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.filename = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error Occured in Python Script [{0}] in line number [{1}] with ERROR Message [{2}]".format(
            self.filename, self.lineno, self.error_message)