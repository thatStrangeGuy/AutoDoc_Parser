from PySide6.QtWidgets import QWidget, QApplication
from PySide6.QtCore import Signal, Slot

from .base_qt_ui.database_record_create_ui import Ui_Form


class DataBaseRecordCreateWidget(QWidget):
    def __init__(self, widget_id):
        super(DataBaseRecordCreateWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.widget_id = widget_id
