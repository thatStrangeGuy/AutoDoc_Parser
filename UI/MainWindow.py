import logging
import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSizePolicy
from PySide6.QtCore import Signal, Slot, QSize, Qt
from .base_qt_ui.MainWindow_multiPage import Ui_Parser_UI
from controllers import file_controler, msgbox_controller, xls_controller
from .title_bar import TitleBar

logger = logging.getLogger('app.MainWindowGUI')


class MainWindow(QMainWindow):
    ErrorMessage_Signal = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()
        self.raw_excel_df = None
        self.raw_xls_chosenColumn = ""
        self.raw_xls_filepath = ""
        self.ui = Ui_Parser_UI()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # self.ui.titlebar = TitleBar()
        # self.setMenuWidget(self.ui.titlebar)

        self.set_window_title_icon()
        self.initialize_connections()

    def set_window_title_icon(self):
        title_icon = QIcon()
        title_icon.addFile(u":/file_open/icons/icons8-template-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(title_icon)

    @Slot(str)
    def open_xls_raw_file(self):
        self.raw_xls_filepath = file_controler.browse_filepath(
            defaultDir=str(Path().absolute().joinpath("raw_files")),
            filter="Excel files files(*.xlsx *.xls)"
        )
        self.ui.xlsRawFilePath_Line.setText(str(self.raw_xls_filepath))

    @Slot()
    def close_MainWindow(self):
        msgbox_controller.show_exit_dialog()

    @Slot()
    def load_raw_excel(self):
        path, message = file_controler.check_filepath(self.raw_xls_filepath, [".xls", ".xlsx"])
        if path is None:
            self.ErrorMessage_Signal.emit(message)
            return
        else:
            self.raw_excel_df = xls_controller.excel_to_dataframe(path.absolute())
            columns = self.raw_excel_df.columns.tolist()
            self.ui.columnList_ComboBox.clear()
            for i in columns:
                self.ui.columnList_ComboBox.addItem(i)
            self.raw_xls_chosenColumn = self.ui.columnList_ComboBox.currentText()

    @Slot()
    def raw_xls_column_choose(self):
        self.raw_xls_chosenColumn = self.ui.columnList_ComboBox.currentText()

    @Slot(str)
    def ErrorMessage(self, msg: str):
        msgbox_controller.show_error_message(msg)

    def initialize_connections(self):
        self.ui.xlsRawFilePathBrowse_Button.clicked.connect(self.open_xls_raw_file)
        self.ui.exit_Button.clicked.connect(self.close_MainWindow)

        # go to pages on left menu
        self.ui.xlsRawImportPage_Button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.xlsRawImport_Page)
        )
        self.ui.databaseEdit_Button_2.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.databaseEdit_Page)
        )
        self.ui.databaseEdit_Button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.databaseEdit_Page)
        )
        self.ui.wordParsePage_Button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.wordParseXls_page)
        )
        self.ui.settingsEdit_Button.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.configEdit_Page)
        )

        self.ui.columnList_ComboBox.currentTextChanged.connect(
            self.raw_xls_column_choose
        )

        self.ui.xlsRawFilePathLoad_Button.clicked.connect(self.load_raw_excel)

        self.ErrorMessage_Signal.connect(msgbox_controller.show_error_message)
        # self.ui.btn_close.clicked.connect(self.close_MainWindow)
