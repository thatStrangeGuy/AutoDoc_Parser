from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QWidget

from UI.base_qt_ui.title_bar import Ui_TitleBar
from controllers import msgbox_controller


class TitleBar(QWidget):
    def __init__(self):
        super(TitleBar, self).__init__()
        self.ui = Ui_TitleBar()
        self.ui.setupUi(self)
        self.drag_start_position = None
        self.initialize_connections()

    def initialize_connections(self):
        self.ui.btn_close.clicked.connect(self.close_MainWindow)

    @Slot()
    def close_MainWindow(self):
        msgbox_controller.show_exit_dialog()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.globalPos() - self.parent().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            if self.drag_start_position is not None:
                self.parent().move(event.globalPos() - self.drag_start_position)
                event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drag_start_position = None
            event.accept()


