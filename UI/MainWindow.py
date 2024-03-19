from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Signal, Slot
from .base_qt_ui.MainWindow_multiPage import Ui_Parser_UI


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Parser_UI()
        self.ui.setupUi(self)
