import logging
import inspect
class BaseClass:
    def getLooger(self):
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        fileHandler=logging.FileHandler('logfile_report.log')
        formatter=logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger