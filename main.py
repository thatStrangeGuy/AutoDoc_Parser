import logging
import logging.handlers
from pathlib import Path
from controllers.main_init_controller import init_check

init_check()
from controllers import config_controller, db_controller
from PySide6.QtWidgets import QApplication
import sys
from UI.MainWindow import MainWindow


def logger_filter():
    return 0


def init_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    FORMAT = '%(asctime)s :: %(name)s:%(lineno)s :: %(levelname)s :: %(message)s'
    # sh = logging.StreamHandler()
    # sh.setLevel(logging.DEBUG)
    # sh.setFormatter(logging.Formatter(FORMAT))
    fh = logging.handlers.RotatingFileHandler(filename='logs/log.log', maxBytes=10000, backupCount=20, encoding='utf-8')
    fh.setLevel(logging.INFO)
    fh.setFormatter(logging.Formatter(FORMAT))
    # logger.addHandler(sh)
    logger.addHandler(fh)


init_logger("app")
logger = logging.getLogger('app.main')


def main():
    app = QApplication()
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
