import inspect
import logging

import pytest


@pytest.mark.usefixtures("invoke_browser")
class BaseClass:

    def Get_log(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        filehandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        filehandler.setFormatter(formatter)

        logger.addHandler(filehandler)

        logger.setLevel(logging.DEBUG)
        return logger


    def wait(self):
        self.driver.implicitly_wait(9)