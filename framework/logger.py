# coding=utf-8
import logging


def new_line(log_method_function):
    def add_new_line(message):
        log_method_function(message=message)

    return add_new_line


class Logger(object):
    __logger = logging.getLogger("Logger")
    logging.basicConfig(level=logging.INFO, filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s',
                        datefmt='%d-%m-%y %H:%M:%S',
                        filename="protei_testing_api_nominatim/tests/logs/logs.txt", force=True)

    @staticmethod
    def set_level(level):
        Logger.__logger.setLevel(level)

    @staticmethod
    @new_line
    def info(message):
        Logger.__logger.info(msg=message)

    @staticmethod
    @new_line
    def debug(message):
        Logger.__logger.debug(msg=message)

    @staticmethod
    @new_line
    def warning(message):
        Logger.__logger.warning(msg=message)

    @staticmethod
    @new_line
    def error(message):
        Logger.__logger.error(msg=message)

    @staticmethod
    @new_line
    def fatal(message):
        Logger.__logger.fatal(msg=message)

    @staticmethod
    @new_line
    def step(message):
        Logger.__logger.info(msg=message)
