# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
from UI.base_qt_ui import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(792, 595)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background-color: #171a21; /* Steam's Dark Theme Background Color */\n"
"    color: #c6d4df; /* Steam's Text Color */\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QLabel {\n"
"    background-color: #1b2838; /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background-color: #1b2838; /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2d435e; /* Darker shade on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #122031; /* Darker shade when pressed */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #1c2735; /* Steam's Input Field Color */\n"
"    border: 1px solid #1c2735;\n"
"    padding: 5px;\n"
"    color: #c6d"
                        "4df; /* Steam's Text Color */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #5a90d8; /* Steam's Accent Color on focus */\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background-color: #1c2735; /* Steam's Input Field Color */\n"
"    border: 1px solid #1c2735;\n"
"    padding: 5px;\n"
"    color: #c6d4df; /* Steam's Text Color */\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid #5a90d8; /* Steam's Accent Color on focus */\n"
"}\n"
"\n"
"QScrollBar:vertical {\n"
"    border: none;\n"
"    background: #171a21; /* Steam's Scroll Bar Background */\n"
"    width: 12px;\n"
"    margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #5a90d8; /* Steam's Scroll Bar Handle */\n"
"    min-height: 20px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, Q"
                        "ScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid #5a90d8; /* Border color */\n"
"    border-radius: 5px;\n"
"    background-color: #1c2735; /* Background color of the bar */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #5a90d8; /* Color of the progress */\n"
"    width: 20px; /* Width of each progress chunk */\n"
"}\n"
"QRadioButton {\n"
"    color: #c6d4df; /* Text color */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 14px; /* Size of the radio button */\n"
"    height: 14px;\n"
"    border: 2px solid #5a90d8; /* Border color of the radio button */\n"
"    border-radius: 7px; /* Makes it round */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #5a90d8; /* Color when checked */\n"
"    border: 2px solid #5a90d8; /* Border color when checked */\n"
"}\n"
"\n"
"QRadioButton::indicator:hover {\n"
"    border: 2px solid #5a90d8; /* Border color on hover */\n"
"}\n"
"QCh"
                        "eckBox {\n"
"    color: #c6d4df; /* Text color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 14px; /* Size of the checkbox */\n"
"    height: 14px;\n"
"    border: 2px solid #5a90d8; /* Border color of the checkbox */\n"
"    border-radius: 3px; /* Makes it slightly rounded */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-color: #5a90d8; /* Color when checked */\n"
"    border: 2px solid #5a90d8; /* Border color when checked */\n"
"}\n"
"\n"
"QCheckBox::indicator:hover {\n"
"    border: 2px solid #5a90d8; /* Border color on hover */\n"
"}\n"
"QDialogButtonBox {\n"
"    background-color: #1c2735; /* Background color */\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton {\n"
"    background-color: #7289da; /* Button background color */\n"
"    color: #ffffff; /* Button text color */\n"
"    border: 1px solid #7289da; /* Button border color */\n"
"    border-radius: 4px;\n"
"    padding: 5px 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:hover {\n"
"    backgrou"
                        "nd-color: #677bc4; /* Darker shade on hover */\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:pressed {\n"
"    background-color: #5865a6; /* Darker shade when pressed */\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.xlsRawFileImport_Frame = QFrame(self.centralwidget)
        self.xlsRawFileImport_Frame.setObjectName(u"xlsRawFileImport_Frame")
        self.xlsRawFileImport_Frame.setGeometry(QRect(70, 80, 319, 423))
        self.xlsRawFileImport_Frame.setFrameShape(QFrame.StyledPanel)
        self.xlsRawFileImport_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.xlsRawFileImport_Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.xlsRawFileImport_LabelButton = QPushButton(self.xlsRawFileImport_Frame)
        self.xlsRawFileImport_LabelButton.setObjectName(u"xlsRawFileImport_LabelButton")
        self.xlsRawFileImport_LabelButton.setEnabled(False)
        icon = QIcon()
        icon.addFile(u":/file_open/icons/icons8-excel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsRawFileImport_LabelButton.setIcon(icon)

        self.verticalLayout.addWidget(self.xlsRawFileImport_LabelButton)

        self.parseRawExcel_CheckBox = QCheckBox(self.xlsRawFileImport_Frame)
        self.parseRawExcel_CheckBox.setObjectName(u"parseRawExcel_CheckBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.parseRawExcel_CheckBox.sizePolicy().hasHeightForWidth())
        self.parseRawExcel_CheckBox.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.parseRawExcel_CheckBox)

        self.xlsRawFileBrowseFrame = QFrame(self.xlsRawFileImport_Frame)
        self.xlsRawFileBrowseFrame.setObjectName(u"xlsRawFileBrowseFrame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(2)
        sizePolicy1.setHeightForWidth(self.xlsRawFileBrowseFrame.sizePolicy().hasHeightForWidth())
        self.xlsRawFileBrowseFrame.setSizePolicy(sizePolicy1)
        self.xlsRawFileBrowseFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsRawFileBrowseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.xlsRawFileBrowseFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.xlsRawFilePath_Line = QLineEdit(self.xlsRawFileBrowseFrame)
        self.xlsRawFilePath_Line.setObjectName(u"xlsRawFilePath_Line")
        self.xlsRawFilePath_Line.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(6)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.xlsRawFilePath_Line.sizePolicy().hasHeightForWidth())
        self.xlsRawFilePath_Line.setSizePolicy(sizePolicy2)
        self.xlsRawFilePath_Line.setReadOnly(True)

        self.horizontalLayout.addWidget(self.xlsRawFilePath_Line)

        self.xlsRawFilePathBrowse_Button = QPushButton(self.xlsRawFileBrowseFrame)
        self.xlsRawFilePathBrowse_Button.setObjectName(u"xlsRawFilePathBrowse_Button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.xlsRawFilePathBrowse_Button.sizePolicy().hasHeightForWidth())
        self.xlsRawFilePathBrowse_Button.setSizePolicy(sizePolicy3)
        self.xlsRawFilePathBrowse_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        icon1 = QIcon()
        icon1.addFile(u":/file_open/icons/icons8-open-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsRawFilePathBrowse_Button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.xlsRawFilePathBrowse_Button)

        self.xlsRawFilePathLoad_Button = QPushButton(self.xlsRawFileBrowseFrame)
        self.xlsRawFilePathLoad_Button.setObjectName(u"xlsRawFilePathLoad_Button")
        sizePolicy3.setHeightForWidth(self.xlsRawFilePathLoad_Button.sizePolicy().hasHeightForWidth())
        self.xlsRawFilePathLoad_Button.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u":/file_open/icons/icons8-download-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsRawFilePathLoad_Button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.xlsRawFilePathLoad_Button)


        self.verticalLayout.addWidget(self.xlsRawFileBrowseFrame)

        self.columnChoose_Frame = QFrame(self.xlsRawFileImport_Frame)
        self.columnChoose_Frame.setObjectName(u"columnChoose_Frame")
        self.columnChoose_Frame.setFrameShape(QFrame.StyledPanel)
        self.columnChoose_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.columnChoose_Frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.coulumnChoose_LabelButton = QPushButton(self.columnChoose_Frame)
        self.coulumnChoose_LabelButton.setObjectName(u"coulumnChoose_LabelButton")
        self.coulumnChoose_LabelButton.setEnabled(False)

        self.horizontalLayout_8.addWidget(self.coulumnChoose_LabelButton)

        self.columnList_ComboBox = QComboBox(self.columnChoose_Frame)
        self.columnList_ComboBox.setObjectName(u"columnList_ComboBox")

        self.horizontalLayout_8.addWidget(self.columnList_ComboBox)


        self.verticalLayout.addWidget(self.columnChoose_Frame)

        self.jsonFileBrowse_LabelButton = QPushButton(self.xlsRawFileImport_Frame)
        self.jsonFileBrowse_LabelButton.setObjectName(u"jsonFileBrowse_LabelButton")
        self.jsonFileBrowse_LabelButton.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/file_open/icons/icons8-json-file-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.jsonFileBrowse_LabelButton.setIcon(icon3)
        self.jsonFileBrowse_LabelButton.setIconSize(QSize(25, 25))

        self.verticalLayout.addWidget(self.jsonFileBrowse_LabelButton)

        self.jsonFileBrowseFrame = QFrame(self.xlsRawFileImport_Frame)
        self.jsonFileBrowseFrame.setObjectName(u"jsonFileBrowseFrame")
        sizePolicy1.setHeightForWidth(self.jsonFileBrowseFrame.sizePolicy().hasHeightForWidth())
        self.jsonFileBrowseFrame.setSizePolicy(sizePolicy1)
        self.jsonFileBrowseFrame.setFrameShape(QFrame.StyledPanel)
        self.jsonFileBrowseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.jsonFileBrowseFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.jsonRawFilePath_Line = QLineEdit(self.jsonFileBrowseFrame)
        self.jsonRawFilePath_Line.setObjectName(u"jsonRawFilePath_Line")
        self.jsonRawFilePath_Line.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.jsonRawFilePath_Line.sizePolicy().hasHeightForWidth())
        self.jsonRawFilePath_Line.setSizePolicy(sizePolicy2)
        self.jsonRawFilePath_Line.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.jsonRawFilePath_Line)

        self.jsonRawFilePathBrowse_Button = QPushButton(self.jsonFileBrowseFrame)
        self.jsonRawFilePathBrowse_Button.setObjectName(u"jsonRawFilePathBrowse_Button")
        sizePolicy3.setHeightForWidth(self.jsonRawFilePathBrowse_Button.sizePolicy().hasHeightForWidth())
        self.jsonRawFilePathBrowse_Button.setSizePolicy(sizePolicy3)
        self.jsonRawFilePathBrowse_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        self.jsonRawFilePathBrowse_Button.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.jsonRawFilePathBrowse_Button)

        self.jsonRawFilePathLoad_Button = QPushButton(self.jsonFileBrowseFrame)
        self.jsonRawFilePathLoad_Button.setObjectName(u"jsonRawFilePathLoad_Button")
        sizePolicy3.setHeightForWidth(self.jsonRawFilePathLoad_Button.sizePolicy().hasHeightForWidth())
        self.jsonRawFilePathLoad_Button.setSizePolicy(sizePolicy3)
        self.jsonRawFilePathLoad_Button.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.jsonRawFilePathLoad_Button)


        self.verticalLayout.addWidget(self.jsonFileBrowseFrame)

        self.openDictionaryScreen_Button = QPushButton(self.xlsRawFileImport_Frame)
        self.openDictionaryScreen_Button.setObjectName(u"openDictionaryScreen_Button")
        icon4 = QIcon()
        icon4.addFile(u":/file_open/icons/icons8-curly-brackets-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.openDictionaryScreen_Button.setIcon(icon4)
        self.openDictionaryScreen_Button.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.openDictionaryScreen_Button)

        self.xlsParsedFileBrowseFrame = QFrame(self.xlsRawFileImport_Frame)
        self.xlsParsedFileBrowseFrame.setObjectName(u"xlsParsedFileBrowseFrame")
        sizePolicy1.setHeightForWidth(self.xlsParsedFileBrowseFrame.sizePolicy().hasHeightForWidth())
        self.xlsParsedFileBrowseFrame.setSizePolicy(sizePolicy1)
        self.xlsParsedFileBrowseFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsParsedFileBrowseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.xlsParsedFileBrowseFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.xlsParsedFilePath_Line = QLineEdit(self.xlsParsedFileBrowseFrame)
        self.xlsParsedFilePath_Line.setObjectName(u"xlsParsedFilePath_Line")
        self.xlsParsedFilePath_Line.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.xlsParsedFilePath_Line.sizePolicy().hasHeightForWidth())
        self.xlsParsedFilePath_Line.setSizePolicy(sizePolicy2)
        self.xlsParsedFilePath_Line.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.xlsParsedFilePath_Line)

        self.xlsParsedFilePathBrowse_Button = QPushButton(self.xlsParsedFileBrowseFrame)
        self.xlsParsedFilePathBrowse_Button.setObjectName(u"xlsParsedFilePathBrowse_Button")
        sizePolicy3.setHeightForWidth(self.xlsParsedFilePathBrowse_Button.sizePolicy().hasHeightForWidth())
        self.xlsParsedFilePathBrowse_Button.setSizePolicy(sizePolicy3)
        self.xlsParsedFilePathBrowse_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        self.xlsParsedFilePathBrowse_Button.setIcon(icon1)

        self.horizontalLayout_7.addWidget(self.xlsParsedFilePathBrowse_Button)


        self.verticalLayout.addWidget(self.xlsParsedFileBrowseFrame)

        self.parseToXlsFile_Button = QPushButton(self.xlsRawFileImport_Frame)
        self.parseToXlsFile_Button.setObjectName(u"parseToXlsFile_Button")
        icon5 = QIcon()
        icon5.addFile(u":/file_open/icons/icons8-export-excel-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parseToXlsFile_Button.setIcon(icon5)
        self.parseToXlsFile_Button.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.parseToXlsFile_Button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 792, 22))
        MainWindow.setMenuBar(self.menuBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.xlsRawFileImport_LabelButton.setText(QCoreApplication.translate("MainWindow", u"Raw Excel File Import", None))
        self.parseRawExcel_CheckBox.setText(QCoreApplication.translate("MainWindow", u"Parse Raw Excel?", None))
        self.xlsRawFilePath_Line.setText("")
        self.xlsRawFilePath_Line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click browse to find xls File", None))
        self.xlsRawFilePathBrowse_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.xlsRawFilePathLoad_Button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.coulumnChoose_LabelButton.setText(QCoreApplication.translate("MainWindow", u"Choose Column of ID", None))
        self.jsonFileBrowse_LabelButton.setText(QCoreApplication.translate("MainWindow", u"Json Dictionary Load", None))
        self.jsonRawFilePath_Line.setText("")
        self.jsonRawFilePath_Line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Click browse to find Dictionary File", None))
        self.jsonRawFilePathBrowse_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.jsonRawFilePathLoad_Button.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.openDictionaryScreen_Button.setText(QCoreApplication.translate("MainWindow", u"Edit Dictionary", None))
        self.xlsParsedFilePath_Line.setText("")
        self.xlsParsedFilePath_Line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Where to save Excel File", None))
        self.xlsParsedFilePathBrowse_Button.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.parseToXlsFile_Button.setText(QCoreApplication.translate("MainWindow", u"Parse to xls file", None))
    # retranslateUi

