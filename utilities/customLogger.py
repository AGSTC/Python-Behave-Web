import logging

logger = logging.getLogger()
log_level = ""
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
fh = logging.FileHandler("./Logs/TestReport.log")


class Logger:
    @staticmethod
    def log_info(message):
        logger.setLevel(logging.INFO)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        logger.info(message)




