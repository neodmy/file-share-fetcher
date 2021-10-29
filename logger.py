import logging


class Logger:
    @staticmethod
    def create_logger():
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        custom_format = logging.Formatter('%(asctime)s | %(levelname)s | file-share-fetcher | %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(custom_format)
        logger.addHandler(handler)
        return logger
