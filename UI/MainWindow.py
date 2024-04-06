import logging
import sys
from pathlib import Path

from PySide6.QtGui import QIcon, QMouseEvent
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QSizePolicy, QComboBox, QSizeGrip
from PySide6.QtCore import Signal, Slot, QSize, Qt
from UI.base_qt_ui.MainWindow_multiPage import Ui_Parser_UI
from controllers import file_controler, msgbox_controller, xls_controller, db_controller, config_controller
from controllers.FunctionWrapper import FunctionWrapper
from .base_qt_ui.title_bar import Ui_TitleBar

logger = logging.getLogger('app.MainWindowGUI')

config = config_controller.read_config('config.yaml')


class MainWindow(QMainWindow):
    InfoMessage_Signal = Signal(str, str)
    ActionMessage2_Signal = Signal(str, str, str, FunctionWrapper, str, FunctionWrapper)
    ErrorMessage_Signal = Signal(str)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.raw_excel_df = None
        self.raw_xls_chosenColumn = ""
        self.raw_xls_filepath = ""
        self.ui = Ui_Parser_UI()
        self.ui.setupUi(self)

        # Access the titlebar_frame as a QWidget
        # self.custom_titlebar = self.ui.titlebar_widget

        # Add custom methods or connect signals for the custom title bar
        # self.custom_titlebar.mousePressEvent = self.titlebar_mousePressEvent
        # self.custom_titlebar.mouseMoveEvent = self.move_window
        # self.custom_titlebar.mouseDoubleClickEvent = self.doubleClickTitle
        # self.custom_titlebar.mouseReleaseEvent = self.release_window
        # self.custom_titlebar.setMouseTracking(True)
        # self.maximize_threshold = 10  # Adjust as needed
        # self.click_position = None
        # self.should_maximize = False
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

        # self.ui.titlebar = TitleBar()
        # self.setMenuWidget(self.ui.titlebar)

        self.set_window_title_icon()
        self.initialize_connections()
        self.ui.stackedWidget.setCurrentWidget(self.ui.xlsRawImport_Page)
        self.refresh_page_data()
        self.closeEvent = self.close_MainWindow

        # self.setWindowFlags(self.windowFlags() | Qt.WindowMinimizeButtonHint)
        # self.size_grips = [
        #     QSizeGrip(self),
        #     QSizeGrip(self),
        #     QSizeGrip(self),
        #     QSizeGrip(self)
        # ]
        #
        # self.size_grips[0].setStyleSheet("background-color: rgb(255, 0, 0)")
        # self.size_grips[1].setStyleSheet("background-color: rgb(255, 0, 0)")
        # self.size_grips[2].setStyleSheet("background-color: rgb(255, 0, 0)")
        # self.size_grips[3].setStyleSheet("background-color: rgb(255, 0, 0)")
        #
        # # Add size grip to bottom-left corner
        # self.size_grips[0].setCursor(Qt.SizeBDiagCursor)
        # self.size_grips[0].resize(20, 20)
        # self.size_grips[0].move(0, self.height() - 20)
        #
        # # Add size grip to top-left corner
        # self.size_grips[1].setCursor(Qt.SizeFDiagCursor)
        # self.size_grips[1].resize(20, 20)
        # self.size_grips[1].move(0, 0)
        #
        # # Add size grip to bottom-right corner
        # self.size_grips[2].setCursor(Qt.SizeFDiagCursor)
        # self.size_grips[2].resize(20, 20)
        # self.size_grips[2].move(self.width() - 20, self.height() - 20)
        #
        # # Add size grip to top-right corner
        # self.size_grips[3].setCursor(Qt.SizeBDiagCursor)
        # self.size_grips[3].resize(20, 20)
        # self.size_grips[3].move(self.width() - 20, 0)

    # def resizeEvent(self, event):
    #     for grip in self.size_grips:
    #         grip.move(self.width() - 20, self.height() - 20)

    # def doubleClickTitle(self, *args):
    #     self.maximize_or_normal()
    #
    # def titlebar_mousePressEvent(self, event: QMouseEvent):
    #     if event.button() == Qt.MouseButton.LeftButton:
    #         self.click_position = event.globalPos()
    #
    # def move_window(self, event: QMouseEvent):
    #     if not self.isMaximized() and event.buttons() == Qt.MouseButton.LeftButton:
    #         self.move(self.pos() + event.globalPos() - self.click_position)
    #         self.click_position = event.globalPos()
    #         current_pos = self.mapToGlobal(event.pos())
    #         if current_pos.y() < 0 < current_pos.x():
    #             self.should_maximize = True
    #         else:
    #             self.should_maximize = False
    #         event.accept()
    #     elif self.isMaximized() and event.buttons() == Qt.MouseButton.LeftButton:
    #         diff = event.globalPos() - self.click_position
    #         if diff.manhattanLength() > self.maximize_threshold:
    #             self.showNormal()
    #             self.move(self.pos() + diff)
    #             self.click_position = event.globalPos()
    #             event.accept()
    #
    # def release_window(self, event: QMouseEvent):
    #     if self.should_maximize:
    #         self.showMaximized()
    #     event.accept()

    def set_window_title_icon(self):
        title_icon = QIcon()
        title_icon.addFile(u":/file_open/icons/icons8-template-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(title_icon)

    @Slot(str)
    def open_xls_raw_file(self):
        self.ui.columnList_ComboBox.clear()
        self.raw_xls_filepath = file_controler.browse_filepath(
            defaultDir=str(Path().absolute().joinpath("raw_files")),
            filter="Excel files files(*.xlsx *.xls)"
        )
        self.ui.xlsRawFilePath_Line.setText(str(self.raw_xls_filepath))

    @Slot()
    def close_MainWindow(self, event=None):
        msgbox_controller.show_exit_dialog(event)

    def closeEvent(self, event) -> None:
        self.close_MainWindow(event)

    @Slot()
    def load_raw_excel(self):
        path, message = file_controler.check_filepath(self.raw_xls_filepath, [".xls", ".xlsx"])
        if path is None:
            self.ErrorMessage_Signal.emit(message)
            return
        else:
            self.raw_excel_df, error = xls_controller.excel_to_dataframe(path.absolute())
            if self.raw_excel_df is None:
                self.ErrorMessage_Signal.emit(error)
                return
            else:
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
        self.ActionMessage2_Signal.connect(msgbox_controller.show_2action_message)
        self.InfoMessage_Signal.connect(msgbox_controller.show_info_message)

        self.ui.stackedWidget.currentChanged.connect(self.refresh_page_data)

        # self.ui.btn_close.clicked.connect(self.close_MainWindow)
        # self.ui.btn_maximize_restore.clicked.connect(self.maximize_or_normal)
        # self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())

        self.ui.DatabaseEditRestoreDefault_Button.clicked.connect(self.restore_default_config)



    def maximize_or_normal(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def __check_databases_ui(self):
        databases, error = db_controller.get_sqlite_databases(config.get('db_dir'))
        if databases is None:
            self.ErrorMessage_Signal.emit(error)
        elif len(databases) == 0:
            self.create_First_db()
        elif len(databases) > 0:
            self.fill_list_combobox(self.ui.DatabaseChoice_ComboBox, databases)

    @Slot()
    def refresh_page_data(self):
        global config

        # xlsRawImport_Page
        if self.ui.stackedWidget.currentWidget() == self.ui.xlsRawImport_Page:
            self.__check_databases_ui()

        # databaseEdit_Page
        elif self.ui.stackedWidget.currentWidget() == self.ui.databaseEdit_Page:
            print("Current page is editing database")  # TODO: Refreshing page if current page is editing database

        # wordParseXls_page
        elif self.ui.stackedWidget.currentWidget() == self.ui.wordParseXls_page:
            print("Current page is parse word")  # TODO: Refreshing page if current page is Word Parsing page

        # configEdit_Page
        elif self.ui.stackedWidget.currentWidget() == self.ui.configEdit_Page:
            print("Current page is config page")  # TODO: Refreshing page if current page is config editing page

    @Slot()
    def restore_default_config(self):
        global config
        yes_action = FunctionWrapper(config_controller.restore_default_config)
        no_action = FunctionWrapper(print, None)
        self.ActionMessage2_Signal.emit(
            "You sure you want to restore default config?",
            "",
            "Yes",
            yes_action,
            "No",
            no_action
        )
        if isinstance(yes_action.result, list):
            result, error = yes_action.result
            if result is None:
                self.ErrorMessage_Signal.emit(error)
            else:
                self.InfoMessage_Signal.emit(result, "")
                self.refresh_page_data()

    def create_First_db(self):
        db_path = config.get('db_path')
        path, error = file_controler.check_filepath_nonExist(db_path, ['.db'])
        if path is None:
            self.ErrorMessage_Signal.emit(error)
        else:
            yes_action = FunctionWrapper(db_controller.CreateDatabase, Path(path).resolve())
            no_action = FunctionWrapper(print, None)
            self.ActionMessage2_Signal.emit(
                "No databases found, would you like to create a default one?",
                "",
                "Yes",
                yes_action,
                "No",
                no_action
            )
            if isinstance(yes_action.result, list):
                result, error = yes_action.result
                if result is None:
                    self.ErrorMessage_Signal.emit(error)
                else:
                    self.InfoMessage_Signal.emit(result, "")

    @staticmethod
    def fill_list_combobox(combobox: QComboBox, data: list | tuple):
        combobox.clear()
        for i in data:
            if isinstance(i, Path):
                i = i.stem
            combobox.addItem(i)
            combobox.setCurrentIndex(0)
