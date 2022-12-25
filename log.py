import os
import logging
import time
from logging.handlers import RotatingFileHandler
from config import config

# log configuration to automatically generate log files by date
def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)


def getLogHandler(config_name):
    # log address
    log_dir_name = "Logs"
    # File name, with the date as the file name
    log_file_name = 'logger-' + time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    # Create a log file
    log_file_folder = os.path.abspath(
        os.path.join(os.path.dirname(__file__), os.pardir)) + os.sep + log_dir_name
    make_dir(log_file_folder)
    log_file_str = log_file_folder + os.sep + log_file_name

    # Setting the default log level
    logging.basicConfig(level=config[config_name].LOG_LEVEL)
    # Create a logger, specify the log save path, the size of each log, and the upper limit of the log save
    file_log_handler = RotatingFileHandler(log_file_str, maxBytes=1024 * 1024 * 100, backupCount=100, encoding='UTF-8')
    # setting log format           occurrence time log level     log filename    function name  line number log message
    formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')
    # The logger specifies the format of the log
    file_log_handler.setFormatter(formatter)

    logging.getLogger().addHandler(file_log_handler)
    return file_log_handler
