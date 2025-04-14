import logging
import os
import sys

# Make a dir in the root directory of the project
log_dir = os.path.join(os.getcwd(), 'logs')
os.makedirs(log_dir, exist_ok=True)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

# Create a StreamHandler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

# Create a FileHandler
def get_file_handler():
    # Get the filename of the script that logs the message
    caller_filename = os.path.splitext(os.path.basename(sys.argv[0]))[0]
    log_file = os.path.join(log_dir, f"{caller_filename}.log")
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setFormatter(formatter)
    return file_handler

logger.addHandler(get_file_handler())

def logging():
    exc_type, exc_obj, exc_tb = sys.exc_info()
    logger.warning("--------------------------------------------------")
    logger.error("Oops! An exception has occurred: " + str(exc_obj))
    if exc_tb is not None:
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger.error("File Name: " + fname)
        logger.error("Line Number: " + str(exc_tb.tb_lineno))
    logger.error("Exception TYPE: " + str(exc_type))
    logger.warning("--------------------------------------------------")