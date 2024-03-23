# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow_multiPage.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QFrame, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QVBoxLayout, QWidget)
from UI.base_qt_ui import icons_rc

class Ui_Parser_UI(object):
    def setupUi(self, Parser_UI):
        if not Parser_UI.objectName():
            Parser_UI.setObjectName(u"Parser_UI")
        Parser_UI.setWindowModality(Qt.ApplicationModal)
        Parser_UI.resize(823, 722)
        Parser_UI.setStyleSheet(u"QWidget {\n"
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
"\n"
"QToolTip {\n"
"    border: 1px solid #c8c8c8;\n"
"	background-color: #171a21; /* Steam's Dark Theme Background Color */\n"
"    color: #c6d4df; /* Steam's Text Color */\n"
"    font-size: 12px;\n"
"	border-radius:5px;\n"
"    }")
        Parser_UI.setToolButtonStyle(Qt.ToolButtonTextOnly)
        Parser_UI.setDocumentMode(True)
        Parser_UI.setTabShape(QTabWidget.Rounded)
        Parser_UI.setUnifiedTitleAndToolBarOnMac(False)
        self.actiontest3 = QAction(Parser_UI)
        self.actiontest3.setObjectName(u"actiontest3")
        self.actiontest4 = QAction(Parser_UI)
        self.actiontest4.setObjectName(u"actiontest4")
        self.centralwidget = QWidget(Parser_UI)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"Line{\n"
"	color: #FFFFFF;\n"
"}")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_2.addWidget(self.line)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titlebar_frame = QFrame(self.frame)
        self.titlebar_frame.setObjectName(u"titlebar_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.titlebar_frame.sizePolicy().hasHeightForWidth())
        self.titlebar_frame.setSizePolicy(sizePolicy)
        self.titlebar_frame.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	border-radius: 8px;\n"
"	max-width: 16px;\n"
"	max-height: 16px;\n"
"    padding: 0;\n"
"    margin: 0;\n"
"    border: 0;\n"
"}\n"
"#btn_minimize {\n"
"    background-color: #4AE137;\n"
"}\n"
"#btn_minimize:hover {\n"
"    background-color: #4DFD36;\n"
"}\n"
"#btn_minimize:pressed {\n"
"    background-color: #21A80F;\n"
"}\n"
"\n"
"#btn_maximize_restore {\n"
"    background-color: #FDCE36;\n"
"}\n"
"\n"
"#btn_maximize_restore:hover {\n"
"    background-color: #FCFF34;\n"
"}\n"
"#btn_maximize_restore:pressed {\n"
"    background-color: #BCBF05;\n"
"}\n"
"\n"
"#btn_close {\n"
"    background-color: #D54040;\n"
"}\n"
"#btn_close:hover {\n"
"    background-color: #F82D2D;\n"
"}\n"
"#btn_close:pressed {\n"
"    background-color: #A90808;\n"
"}\n"
"QLabel {\n"
"    font-family: \"Microsoft Sans Serif\", \"Arial\", \"Times New Roman\"; /* Use a fallback font */\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"	border:none;\n"
"	background-color:transparent;\n"
"}")
        self.titlebar_frame.setFrameShape(QFrame.StyledPanel)
        self.titlebar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.titlebar_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.titlebar_frame)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(6)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.titlebar_frame)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(9)
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.leftSideMenu_Frame = QFrame(self.frame_3)
        self.leftSideMenu_Frame.setObjectName(u"leftSideMenu_Frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.leftSideMenu_Frame.sizePolicy().hasHeightForWidth())
        self.leftSideMenu_Frame.setSizePolicy(sizePolicy3)
        self.leftSideMenu_Frame.setFrameShape(QFrame.StyledPanel)
        self.leftSideMenu_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.leftSideMenu_Frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.xlsRawImportPage_Button = QPushButton(self.leftSideMenu_Frame)
        self.xlsRawImportPage_Button.setObjectName(u"xlsRawImportPage_Button")
        self.xlsRawImportPage_Button.setCursor(QCursor(Qt.ArrowCursor))
        self.xlsRawImportPage_Button.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u":/file_open/icons/icons8-excel.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsRawImportPage_Button.setIcon(icon)
        self.xlsRawImportPage_Button.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.xlsRawImportPage_Button)

        self.databaseEdit_Button_2 = QPushButton(self.leftSideMenu_Frame)
        self.databaseEdit_Button_2.setObjectName(u"databaseEdit_Button_2")
        self.databaseEdit_Button_2.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/file_open/icons/icons8-database-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseEdit_Button_2.setIcon(icon1)
        self.databaseEdit_Button_2.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.databaseEdit_Button_2)

        self.wordParsePage_Button = QPushButton(self.leftSideMenu_Frame)
        self.wordParsePage_Button.setObjectName(u"wordParsePage_Button")
        icon2 = QIcon()
        icon2.addFile(u":/file_open/icons/icons8-word-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.wordParsePage_Button.setIcon(icon2)
        self.wordParsePage_Button.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.wordParsePage_Button)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settingsEdit_Button = QPushButton(self.leftSideMenu_Frame)
        self.settingsEdit_Button.setObjectName(u"settingsEdit_Button")
        self.settingsEdit_Button.setEnabled(True)
        icon3 = QIcon()
        icon3.addFile(u":/file_open/icons/icons8-settings-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsEdit_Button.setIcon(icon3)
        self.settingsEdit_Button.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.settingsEdit_Button)

        self.exit_Button = QPushButton(self.leftSideMenu_Frame)
        self.exit_Button.setObjectName(u"exit_Button")
        self.exit_Button.setStyleSheet(u"#exit_Button{\n"
"	background-color:#B00C06;\n"
"}\n"
"#exit_Button:hover{\n"
"	background-color:#E90800;\n"
"}\n"
"#exit_Button:pressed{\n"
"	background-color:#790B07;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/file_open/icons/icons8-exit-80.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exit_Button.setIcon(icon4)
        self.exit_Button.setIconSize(QSize(40, 40))

        self.verticalLayout_2.addWidget(self.exit_Button)


        self.horizontalLayout_11.addWidget(self.leftSideMenu_Frame)

        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(8)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy4)
        self.stackedWidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.xlsRawImport_Page = QWidget()
        self.xlsRawImport_Page.setObjectName(u"xlsRawImport_Page")
        self.horizontalLayout_3 = QHBoxLayout(self.xlsRawImport_Page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.xlsRawFileImport_Frame = QFrame(self.xlsRawImport_Page)
        self.xlsRawFileImport_Frame.setObjectName(u"xlsRawFileImport_Frame")
        self.xlsRawFileImport_Frame.setFrameShape(QFrame.StyledPanel)
        self.xlsRawFileImport_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.xlsRawFileImport_Frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.xlsRawFileImport_MainFrame = QFrame(self.xlsRawFileImport_Frame)
        self.xlsRawFileImport_MainFrame.setObjectName(u"xlsRawFileImport_MainFrame")
        self.xlsRawFileImport_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsRawFileImport_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.xlsRawFileImport_MainFrame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.xlsRawFileImport_LabelButton = QPushButton(self.xlsRawFileImport_MainFrame)
        self.xlsRawFileImport_LabelButton.setObjectName(u"xlsRawFileImport_LabelButton")
        self.xlsRawFileImport_LabelButton.setEnabled(False)
        self.xlsRawFileImport_LabelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        self.xlsRawFileImport_LabelButton.setIcon(icon)

        self.verticalLayout_9.addWidget(self.xlsRawFileImport_LabelButton)

        self.xlsRawFileBrowseFrame = QFrame(self.xlsRawFileImport_MainFrame)
        self.xlsRawFileBrowseFrame.setObjectName(u"xlsRawFileBrowseFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(2)
        sizePolicy5.setHeightForWidth(self.xlsRawFileBrowseFrame.sizePolicy().hasHeightForWidth())
        self.xlsRawFileBrowseFrame.setSizePolicy(sizePolicy5)
        self.xlsRawFileBrowseFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsRawFileBrowseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.xlsRawFileBrowseFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.xlsRawFilePath_Line = QLineEdit(self.xlsRawFileBrowseFrame)
        self.xlsRawFilePath_Line.setObjectName(u"xlsRawFilePath_Line")
        self.xlsRawFilePath_Line.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy6.setHorizontalStretch(6)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.xlsRawFilePath_Line.sizePolicy().hasHeightForWidth())
        self.xlsRawFilePath_Line.setSizePolicy(sizePolicy6)
        self.xlsRawFilePath_Line.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.xlsRawFilePath_Line)

        self.xlsRawFilePathBrowse_Button = QPushButton(self.xlsRawFileBrowseFrame)
        self.xlsRawFilePathBrowse_Button.setObjectName(u"xlsRawFilePathBrowse_Button")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy7.setHorizontalStretch(2)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.xlsRawFilePathBrowse_Button.sizePolicy().hasHeightForWidth())
        self.xlsRawFilePathBrowse_Button.setSizePolicy(sizePolicy7)
        self.xlsRawFilePathBrowse_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        icon5 = QIcon()
        icon5.addFile(u":/file_open/icons/icons8-open-file.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsRawFilePathBrowse_Button.setIcon(icon5)

        self.horizontalLayout_4.addWidget(self.xlsRawFilePathBrowse_Button)

        self.xlsRawFilePathLoad_Button = QPushButton(self.xlsRawFileBrowseFrame)
        self.xlsRawFilePathLoad_Button.setObjectName(u"xlsRawFilePathLoad_Button")
        sizePolicy7.setHeightForWidth(self.xlsRawFilePathLoad_Button.sizePolicy().hasHeightForWidth())
        self.xlsRawFilePathLoad_Button.setSizePolicy(sizePolicy7)
        icon6 = QIcon()
        icon6.addFile(u":/file_open/icons/icons8-download-60.png", QSize(), QIcon.Normal, QIcon.Off)
        self.xlsRawFilePathLoad_Button.setIcon(icon6)

        self.horizontalLayout_4.addWidget(self.xlsRawFilePathLoad_Button)


        self.verticalLayout_9.addWidget(self.xlsRawFileBrowseFrame)

        self.columnChoose_Frame = QFrame(self.xlsRawFileImport_MainFrame)
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


        self.verticalLayout_9.addWidget(self.columnChoose_Frame)


        self.verticalLayout_3.addWidget(self.xlsRawFileImport_MainFrame)

        self.line_2 = QFrame(self.xlsRawFileImport_Frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShadow(QFrame.Raised)
        self.line_2.setLineWidth(20)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_2)

        self.databaseLoad_MainFrame = QFrame(self.xlsRawFileImport_Frame)
        self.databaseLoad_MainFrame.setObjectName(u"databaseLoad_MainFrame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(3)
        sizePolicy8.setHeightForWidth(self.databaseLoad_MainFrame.sizePolicy().hasHeightForWidth())
        self.databaseLoad_MainFrame.setSizePolicy(sizePolicy8)
        self.databaseLoad_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.databaseLoad_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.databaseLoad_MainFrame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.databaseBrowse_LabelButton = QPushButton(self.databaseLoad_MainFrame)
        self.databaseBrowse_LabelButton.setObjectName(u"databaseBrowse_LabelButton")
        self.databaseBrowse_LabelButton.setEnabled(False)
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(1)
        sizePolicy9.setHeightForWidth(self.databaseBrowse_LabelButton.sizePolicy().hasHeightForWidth())
        self.databaseBrowse_LabelButton.setSizePolicy(sizePolicy9)
        self.databaseBrowse_LabelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/file_open/icons/icons8-json-file-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseBrowse_LabelButton.setIcon(icon7)
        self.databaseBrowse_LabelButton.setIconSize(QSize(25, 25))

        self.verticalLayout_4.addWidget(self.databaseBrowse_LabelButton)

        self.databaseConnect_Frame = QFrame(self.databaseLoad_MainFrame)
        self.databaseConnect_Frame.setObjectName(u"databaseConnect_Frame")
        sizePolicy10 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(5)
        sizePolicy10.setHeightForWidth(self.databaseConnect_Frame.sizePolicy().hasHeightForWidth())
        self.databaseConnect_Frame.setSizePolicy(sizePolicy10)
        self.databaseConnect_Frame.setFrameShape(QFrame.StyledPanel)
        self.databaseConnect_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.databaseConnect_Frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.databaseBrowse_Frame = QFrame(self.databaseConnect_Frame)
        self.databaseBrowse_Frame.setObjectName(u"databaseBrowse_Frame")
        sizePolicy11 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(4)
        sizePolicy11.setHeightForWidth(self.databaseBrowse_Frame.sizePolicy().hasHeightForWidth())
        self.databaseBrowse_Frame.setSizePolicy(sizePolicy11)
        self.databaseBrowse_Frame.setMinimumSize(QSize(0, 50))
        self.databaseBrowse_Frame.setStyleSheet(u"")
        self.databaseBrowse_Frame.setFrameShape(QFrame.StyledPanel)
        self.databaseBrowse_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.databaseBrowse_Frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.DatabaseChoice_ComboBox = QComboBox(self.databaseBrowse_Frame)
        self.DatabaseChoice_ComboBox.setObjectName(u"DatabaseChoice_ComboBox")
        sizePolicy12 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy12.setHorizontalStretch(6)
        sizePolicy12.setVerticalStretch(2)
        sizePolicy12.setHeightForWidth(self.DatabaseChoice_ComboBox.sizePolicy().hasHeightForWidth())
        self.DatabaseChoice_ComboBox.setSizePolicy(sizePolicy12)

        self.horizontalLayout_5.addWidget(self.DatabaseChoice_ComboBox)

        self.DatabaseConnect_Button = QPushButton(self.databaseBrowse_Frame)
        self.DatabaseConnect_Button.setObjectName(u"DatabaseConnect_Button")
        sizePolicy13 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy13.setHorizontalStretch(1)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.DatabaseConnect_Button.sizePolicy().hasHeightForWidth())
        self.DatabaseConnect_Button.setSizePolicy(sizePolicy13)
        icon8 = QIcon()
        icon8.addFile(u":/file_open/icons/icons8-connect-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DatabaseConnect_Button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.DatabaseConnect_Button)


        self.verticalLayout_5.addWidget(self.databaseBrowse_Frame)

        self.tableBrowse_Frame = QFrame(self.databaseConnect_Frame)
        self.tableBrowse_Frame.setObjectName(u"tableBrowse_Frame")
        sizePolicy11.setHeightForWidth(self.tableBrowse_Frame.sizePolicy().hasHeightForWidth())
        self.tableBrowse_Frame.setSizePolicy(sizePolicy11)
        self.tableBrowse_Frame.setMinimumSize(QSize(0, 49))
        self.tableBrowse_Frame.setFrameShape(QFrame.StyledPanel)
        self.tableBrowse_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.tableBrowse_Frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.TableChoice_ComboBox = QComboBox(self.tableBrowse_Frame)
        self.TableChoice_ComboBox.setObjectName(u"TableChoice_ComboBox")
        sizePolicy12.setHeightForWidth(self.TableChoice_ComboBox.sizePolicy().hasHeightForWidth())
        self.TableChoice_ComboBox.setSizePolicy(sizePolicy12)

        self.horizontalLayout_6.addWidget(self.TableChoice_ComboBox)

        self.DatabaseConnectionSave_Button = QPushButton(self.tableBrowse_Frame)
        self.DatabaseConnectionSave_Button.setObjectName(u"DatabaseConnectionSave_Button")
        sizePolicy13.setHeightForWidth(self.DatabaseConnectionSave_Button.sizePolicy().hasHeightForWidth())
        self.DatabaseConnectionSave_Button.setSizePolicy(sizePolicy13)
        icon9 = QIcon()
        icon9.addFile(u":/file_open/icons/icons8-save-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DatabaseConnectionSave_Button.setIcon(icon9)

        self.horizontalLayout_6.addWidget(self.DatabaseConnectionSave_Button)


        self.verticalLayout_5.addWidget(self.tableBrowse_Frame)


        self.verticalLayout_4.addWidget(self.databaseConnect_Frame)

        self.databaseEdit_Button = QPushButton(self.databaseLoad_MainFrame)
        self.databaseEdit_Button.setObjectName(u"databaseEdit_Button")
        sizePolicy14 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(1)
        sizePolicy14.setHeightForWidth(self.databaseEdit_Button.sizePolicy().hasHeightForWidth())
        self.databaseEdit_Button.setSizePolicy(sizePolicy14)
        self.databaseEdit_Button.setIcon(icon1)
        self.databaseEdit_Button.setIconSize(QSize(30, 30))

        self.verticalLayout_4.addWidget(self.databaseEdit_Button)


        self.verticalLayout_3.addWidget(self.databaseLoad_MainFrame)

        self.line_3 = QFrame(self.xlsRawFileImport_Frame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShadow(QFrame.Raised)
        self.line_3.setLineWidth(20)
        self.line_3.setMidLineWidth(1)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_3)

        self.xlsParsedFile_MainFrame = QFrame(self.xlsRawFileImport_Frame)
        self.xlsParsedFile_MainFrame.setObjectName(u"xlsParsedFile_MainFrame")
        sizePolicy.setHeightForWidth(self.xlsParsedFile_MainFrame.sizePolicy().hasHeightForWidth())
        self.xlsParsedFile_MainFrame.setSizePolicy(sizePolicy)
        self.xlsParsedFile_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsParsedFile_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.xlsParsedFile_MainFrame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.xlsParsedFileBrowseFrame = QFrame(self.xlsParsedFile_MainFrame)
        self.xlsParsedFileBrowseFrame.setObjectName(u"xlsParsedFileBrowseFrame")
        sizePolicy5.setHeightForWidth(self.xlsParsedFileBrowseFrame.sizePolicy().hasHeightForWidth())
        self.xlsParsedFileBrowseFrame.setSizePolicy(sizePolicy5)
        self.xlsParsedFileBrowseFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsParsedFileBrowseFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.xlsParsedFileBrowseFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.xlsParsedFilePath_Line = QLineEdit(self.xlsParsedFileBrowseFrame)
        self.xlsParsedFilePath_Line.setObjectName(u"xlsParsedFilePath_Line")
        self.xlsParsedFilePath_Line.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.xlsParsedFilePath_Line.sizePolicy().hasHeightForWidth())
        self.xlsParsedFilePath_Line.setSizePolicy(sizePolicy6)
        self.xlsParsedFilePath_Line.setReadOnly(True)

        self.horizontalLayout_7.addWidget(self.xlsParsedFilePath_Line)

        self.xlsParsedFilePathBrowse_Button = QPushButton(self.xlsParsedFileBrowseFrame)
        self.xlsParsedFilePathBrowse_Button.setObjectName(u"xlsParsedFilePathBrowse_Button")
        sizePolicy7.setHeightForWidth(self.xlsParsedFilePathBrowse_Button.sizePolicy().hasHeightForWidth())
        self.xlsParsedFilePathBrowse_Button.setSizePolicy(sizePolicy7)
        self.xlsParsedFilePathBrowse_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        self.xlsParsedFilePathBrowse_Button.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.xlsParsedFilePathBrowse_Button)


        self.verticalLayout_8.addWidget(self.xlsParsedFileBrowseFrame)

        self.parseToXlsFile_Button = QPushButton(self.xlsParsedFile_MainFrame)
        self.parseToXlsFile_Button.setObjectName(u"parseToXlsFile_Button")
        self.parseToXlsFile_Button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0,255,0,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(120,120,120,30); /* Darker shade on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #122031; /* Darker shade when pressed */\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/file_open/icons/icons8-export-excel-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parseToXlsFile_Button.setIcon(icon10)
        self.parseToXlsFile_Button.setIconSize(QSize(20, 20))

        self.verticalLayout_8.addWidget(self.parseToXlsFile_Button)


        self.verticalLayout_3.addWidget(self.xlsParsedFile_MainFrame)


        self.horizontalLayout_3.addWidget(self.xlsRawFileImport_Frame)

        self.stackedWidget.addWidget(self.xlsRawImport_Page)
        self.databaseEdit_Page = QWidget()
        self.databaseEdit_Page.setObjectName(u"databaseEdit_Page")
        self.verticalLayout_11 = QVBoxLayout(self.databaseEdit_Page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.databaseConnect_Frame_2 = QFrame(self.databaseEdit_Page)
        self.databaseConnect_Frame_2.setObjectName(u"databaseConnect_Frame_2")
        sizePolicy5.setHeightForWidth(self.databaseConnect_Frame_2.sizePolicy().hasHeightForWidth())
        self.databaseConnect_Frame_2.setSizePolicy(sizePolicy5)
        self.databaseConnect_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.databaseConnect_Frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.databaseConnect_Frame_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.databaseEdit_label = QPushButton(self.databaseConnect_Frame_2)
        self.databaseEdit_label.setObjectName(u"databaseEdit_label")
        self.databaseEdit_label.setEnabled(False)
        self.databaseEdit_label.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        self.databaseEdit_label.setIcon(icon1)

        self.verticalLayout_10.addWidget(self.databaseEdit_label)

        self.databaseBrowse_Frame_2 = QFrame(self.databaseConnect_Frame_2)
        self.databaseBrowse_Frame_2.setObjectName(u"databaseBrowse_Frame_2")
        sizePolicy5.setHeightForWidth(self.databaseBrowse_Frame_2.sizePolicy().hasHeightForWidth())
        self.databaseBrowse_Frame_2.setSizePolicy(sizePolicy5)
        self.databaseBrowse_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.databaseBrowse_Frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.databaseBrowse_Frame_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.DatabaseChoice_ComboBox_2 = QComboBox(self.databaseBrowse_Frame_2)
        self.DatabaseChoice_ComboBox_2.setObjectName(u"DatabaseChoice_ComboBox_2")
        sizePolicy15 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy15.setHorizontalStretch(8)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.DatabaseChoice_ComboBox_2.sizePolicy().hasHeightForWidth())
        self.DatabaseChoice_ComboBox_2.setSizePolicy(sizePolicy15)
        self.DatabaseChoice_ComboBox_2.setEditable(True)

        self.horizontalLayout_9.addWidget(self.DatabaseChoice_ComboBox_2)

        self.DatabaseConnect_Button_2 = QPushButton(self.databaseBrowse_Frame_2)
        self.DatabaseConnect_Button_2.setObjectName(u"DatabaseConnect_Button_2")
        sizePolicy13.setHeightForWidth(self.DatabaseConnect_Button_2.sizePolicy().hasHeightForWidth())
        self.DatabaseConnect_Button_2.setSizePolicy(sizePolicy13)
        self.DatabaseConnect_Button_2.setIcon(icon8)

        self.horizontalLayout_9.addWidget(self.DatabaseConnect_Button_2)

        self.DatabaseCreate_Button = QPushButton(self.databaseBrowse_Frame_2)
        self.DatabaseCreate_Button.setObjectName(u"DatabaseCreate_Button")
        sizePolicy13.setHeightForWidth(self.DatabaseCreate_Button.sizePolicy().hasHeightForWidth())
        self.DatabaseCreate_Button.setSizePolicy(sizePolicy13)
        icon11 = QIcon()
        icon11.addFile(u":/file_open/icons/icons8-add-database-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.DatabaseCreate_Button.setIcon(icon11)

        self.horizontalLayout_9.addWidget(self.DatabaseCreate_Button)


        self.verticalLayout_10.addWidget(self.databaseBrowse_Frame_2)

        self.tableBrowse_Frame_2 = QFrame(self.databaseConnect_Frame_2)
        self.tableBrowse_Frame_2.setObjectName(u"tableBrowse_Frame_2")
        sizePolicy5.setHeightForWidth(self.tableBrowse_Frame_2.sizePolicy().hasHeightForWidth())
        self.tableBrowse_Frame_2.setSizePolicy(sizePolicy5)
        self.tableBrowse_Frame_2.setFrameShape(QFrame.StyledPanel)
        self.tableBrowse_Frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.tableBrowse_Frame_2)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.TableChoice_ComboBox_2 = QComboBox(self.tableBrowse_Frame_2)
        self.TableChoice_ComboBox_2.setObjectName(u"TableChoice_ComboBox_2")
        sizePolicy15.setHeightForWidth(self.TableChoice_ComboBox_2.sizePolicy().hasHeightForWidth())
        self.TableChoice_ComboBox_2.setSizePolicy(sizePolicy15)
        self.TableChoice_ComboBox_2.setEditable(True)

        self.horizontalLayout_10.addWidget(self.TableChoice_ComboBox_2)

        self.DatabaseConnectionSave_Button_2 = QPushButton(self.tableBrowse_Frame_2)
        self.DatabaseConnectionSave_Button_2.setObjectName(u"DatabaseConnectionSave_Button_2")
        sizePolicy13.setHeightForWidth(self.DatabaseConnectionSave_Button_2.sizePolicy().hasHeightForWidth())
        self.DatabaseConnectionSave_Button_2.setSizePolicy(sizePolicy13)
        self.DatabaseConnectionSave_Button_2.setIcon(icon9)

        self.horizontalLayout_10.addWidget(self.DatabaseConnectionSave_Button_2)

        self.tableCreate_Button = QPushButton(self.tableBrowse_Frame_2)
        self.tableCreate_Button.setObjectName(u"tableCreate_Button")
        sizePolicy13.setHeightForWidth(self.tableCreate_Button.sizePolicy().hasHeightForWidth())
        self.tableCreate_Button.setSizePolicy(sizePolicy13)
        icon12 = QIcon()
        icon12.addFile(u":/file_open/icons/icons8-insert-table-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tableCreate_Button.setIcon(icon12)

        self.horizontalLayout_10.addWidget(self.tableCreate_Button)


        self.verticalLayout_10.addWidget(self.tableBrowse_Frame_2)


        self.verticalLayout_11.addWidget(self.databaseConnect_Frame_2)

        self.scrollArea = QScrollArea(self.databaseEdit_Page)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy16 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(8)
        sizePolicy16.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy16)
        self.scrollArea.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"    border: 2px solid #5a90d8; /* Border color */\n"
"    background-color: #171a21; /* Steam's Dark Theme Background Color */\n"
"	border-radius: 5px;\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.scrollArea.setFrameShape(QFrame.Panel)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setLineWidth(3)
        self.scrollArea.setMidLineWidth(2)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 96, 26))
        self.verticalLayout_22 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.databaseRecords_layout = QVBoxLayout()
        self.databaseRecords_layout.setObjectName(u"databaseRecords_layout")

        self.verticalLayout_22.addLayout(self.databaseRecords_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_11.addWidget(self.scrollArea)

        self.databaseReOrder_Button = QPushButton(self.databaseEdit_Page)
        self.databaseReOrder_Button.setObjectName(u"databaseReOrder_Button")
        icon13 = QIcon()
        icon13.addFile(u":/file_open/icons/icons8-sort-96.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseReOrder_Button.setIcon(icon13)

        self.verticalLayout_11.addWidget(self.databaseReOrder_Button)

        self.databaseRegenID_Button = QPushButton(self.databaseEdit_Page)
        self.databaseRegenID_Button.setObjectName(u"databaseRegenID_Button")
        self.databaseRegenID_Button.setIcon(icon13)

        self.verticalLayout_11.addWidget(self.databaseRegenID_Button)

        self.stackedWidget.addWidget(self.databaseEdit_Page)
        self.wordParseXls_page = QWidget()
        self.wordParseXls_page.setObjectName(u"wordParseXls_page")
        self.verticalLayout_7 = QVBoxLayout(self.wordParseXls_page)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.xlsParsedFileImport_MainFrame = QFrame(self.wordParseXls_page)
        self.xlsParsedFileImport_MainFrame.setObjectName(u"xlsParsedFileImport_MainFrame")
        self.xlsParsedFileImport_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.xlsParsedFileImport_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.xlsParsedFileImport_MainFrame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.xlsParsedFileImport_LabelButton = QPushButton(self.xlsParsedFileImport_MainFrame)
        self.xlsParsedFileImport_LabelButton.setObjectName(u"xlsParsedFileImport_LabelButton")
        self.xlsParsedFileImport_LabelButton.setEnabled(False)
        self.xlsParsedFileImport_LabelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        self.xlsParsedFileImport_LabelButton.setIcon(icon)

        self.verticalLayout_6.addWidget(self.xlsParsedFileImport_LabelButton)

        self.xlsParsedFileImport_Frame_3 = QFrame(self.xlsParsedFileImport_MainFrame)
        self.xlsParsedFileImport_Frame_3.setObjectName(u"xlsParsedFileImport_Frame_3")
        sizePolicy5.setHeightForWidth(self.xlsParsedFileImport_Frame_3.sizePolicy().hasHeightForWidth())
        self.xlsParsedFileImport_Frame_3.setSizePolicy(sizePolicy5)
        self.xlsParsedFileImport_Frame_3.setFrameShape(QFrame.StyledPanel)
        self.xlsParsedFileImport_Frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.xlsParsedFileImport_Frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.xlsParsedFileImport_Line = QLineEdit(self.xlsParsedFileImport_Frame_3)
        self.xlsParsedFileImport_Line.setObjectName(u"xlsParsedFileImport_Line")
        self.xlsParsedFileImport_Line.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.xlsParsedFileImport_Line.sizePolicy().hasHeightForWidth())
        self.xlsParsedFileImport_Line.setSizePolicy(sizePolicy6)
        self.xlsParsedFileImport_Line.setReadOnly(True)

        self.horizontalLayout_12.addWidget(self.xlsParsedFileImport_Line)

        self.xlsParsedFileImportBrowse_Button = QPushButton(self.xlsParsedFileImport_Frame_3)
        self.xlsParsedFileImportBrowse_Button.setObjectName(u"xlsParsedFileImportBrowse_Button")
        sizePolicy7.setHeightForWidth(self.xlsParsedFileImportBrowse_Button.sizePolicy().hasHeightForWidth())
        self.xlsParsedFileImportBrowse_Button.setSizePolicy(sizePolicy7)
        self.xlsParsedFileImportBrowse_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        self.xlsParsedFileImportBrowse_Button.setIcon(icon5)

        self.horizontalLayout_12.addWidget(self.xlsParsedFileImportBrowse_Button)


        self.verticalLayout_6.addWidget(self.xlsParsedFileImport_Frame_3)


        self.verticalLayout_7.addWidget(self.xlsParsedFileImport_MainFrame)

        self.templateWordImport_MainFrame = QFrame(self.wordParseXls_page)
        self.templateWordImport_MainFrame.setObjectName(u"templateWordImport_MainFrame")
        self.templateWordImport_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.templateWordImport_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.templateWordImport_MainFrame)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.templateWordImport_LabelButton = QPushButton(self.templateWordImport_MainFrame)
        self.templateWordImport_LabelButton.setObjectName(u"templateWordImport_LabelButton")
        self.templateWordImport_LabelButton.setEnabled(False)
        self.templateWordImport_LabelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/file_open/icons/icons8-microsoft-word-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.templateWordImport_LabelButton.setIcon(icon14)

        self.verticalLayout_13.addWidget(self.templateWordImport_LabelButton)

        self.templateWordImport_Frame = QFrame(self.templateWordImport_MainFrame)
        self.templateWordImport_Frame.setObjectName(u"templateWordImport_Frame")
        sizePolicy5.setHeightForWidth(self.templateWordImport_Frame.sizePolicy().hasHeightForWidth())
        self.templateWordImport_Frame.setSizePolicy(sizePolicy5)
        self.templateWordImport_Frame.setFrameShape(QFrame.StyledPanel)
        self.templateWordImport_Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.templateWordImport_Frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.templateWordImport_Line = QLineEdit(self.templateWordImport_Frame)
        self.templateWordImport_Line.setObjectName(u"templateWordImport_Line")
        self.templateWordImport_Line.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.templateWordImport_Line.sizePolicy().hasHeightForWidth())
        self.templateWordImport_Line.setSizePolicy(sizePolicy6)
        self.templateWordImport_Line.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.templateWordImport_Line)

        self.templateWordImport_Button = QPushButton(self.templateWordImport_Frame)
        self.templateWordImport_Button.setObjectName(u"templateWordImport_Button")
        sizePolicy7.setHeightForWidth(self.templateWordImport_Button.sizePolicy().hasHeightForWidth())
        self.templateWordImport_Button.setSizePolicy(sizePolicy7)
        self.templateWordImport_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        self.templateWordImport_Button.setIcon(icon5)

        self.horizontalLayout_20.addWidget(self.templateWordImport_Button)


        self.verticalLayout_13.addWidget(self.templateWordImport_Frame)


        self.verticalLayout_7.addWidget(self.templateWordImport_MainFrame)

        self.line_6 = QFrame(self.wordParseXls_page)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Raised)
        self.line_6.setLineWidth(20)
        self.line_6.setMidLineWidth(1)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.line_6)

        self.parseWordFileExport_MainFrame = QFrame(self.wordParseXls_page)
        self.parseWordFileExport_MainFrame.setObjectName(u"parseWordFileExport_MainFrame")
        self.parseWordFileExport_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.parseWordFileExport_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.parseWordFileExport_MainFrame)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.parseWordFileExport_LabelButton = QPushButton(self.parseWordFileExport_MainFrame)
        self.parseWordFileExport_LabelButton.setObjectName(u"parseWordFileExport_LabelButton")
        self.parseWordFileExport_LabelButton.setEnabled(False)
        self.parseWordFileExport_LabelButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        self.parseWordFileExport_LabelButton.setIcon(icon2)

        self.verticalLayout_12.addWidget(self.parseWordFileExport_LabelButton)

        self.parseEveryXlsRow_CheckBox = QCheckBox(self.parseWordFileExport_MainFrame)
        self.parseEveryXlsRow_CheckBox.setObjectName(u"parseEveryXlsRow_CheckBox")

        self.verticalLayout_12.addWidget(self.parseEveryXlsRow_CheckBox)

        self.parseWordFileExport_Frame_4 = QFrame(self.parseWordFileExport_MainFrame)
        self.parseWordFileExport_Frame_4.setObjectName(u"parseWordFileExport_Frame_4")
        sizePolicy5.setHeightForWidth(self.parseWordFileExport_Frame_4.sizePolicy().hasHeightForWidth())
        self.parseWordFileExport_Frame_4.setSizePolicy(sizePolicy5)
        self.parseWordFileExport_Frame_4.setFrameShape(QFrame.StyledPanel)
        self.parseWordFileExport_Frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.parseWordFileExport_Frame_4)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.parseWordFileExport_Line = QLineEdit(self.parseWordFileExport_Frame_4)
        self.parseWordFileExport_Line.setObjectName(u"parseWordFileExport_Line")
        self.parseWordFileExport_Line.setEnabled(True)
        sizePolicy6.setHeightForWidth(self.parseWordFileExport_Line.sizePolicy().hasHeightForWidth())
        self.parseWordFileExport_Line.setSizePolicy(sizePolicy6)
        self.parseWordFileExport_Line.setReadOnly(True)

        self.horizontalLayout_13.addWidget(self.parseWordFileExport_Line)

        self.parseWordFileExport_Button = QPushButton(self.parseWordFileExport_Frame_4)
        self.parseWordFileExport_Button.setObjectName(u"parseWordFileExport_Button")
        sizePolicy7.setHeightForWidth(self.parseWordFileExport_Button.sizePolicy().hasHeightForWidth())
        self.parseWordFileExport_Button.setSizePolicy(sizePolicy7)
        self.parseWordFileExport_Button.setStyleSheet(u".material-icons.orange600 { color: #FB8C00; }")
        self.parseWordFileExport_Button.setIcon(icon5)

        self.horizontalLayout_13.addWidget(self.parseWordFileExport_Button)


        self.verticalLayout_12.addWidget(self.parseWordFileExport_Frame_4)


        self.verticalLayout_7.addWidget(self.parseWordFileExport_MainFrame)

        self.line_7 = QFrame(self.wordParseXls_page)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Raised)
        self.line_7.setLineWidth(20)
        self.line_7.setMidLineWidth(1)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_7.addWidget(self.line_7)

        self.parseWordFileExport_ParseButton = QPushButton(self.wordParseXls_page)
        self.parseWordFileExport_ParseButton.setObjectName(u"parseWordFileExport_ParseButton")
        sizePolicy7.setHeightForWidth(self.parseWordFileExport_ParseButton.sizePolicy().hasHeightForWidth())
        self.parseWordFileExport_ParseButton.setSizePolicy(sizePolicy7)
        self.parseWordFileExport_ParseButton.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(0,255,0,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgba(120,120,120,30); /* Darker shade on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #122031; /* Darker shade when pressed */\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/file_open/icons/icons8-move-through-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.parseWordFileExport_ParseButton.setIcon(icon15)
        self.parseWordFileExport_ParseButton.setIconSize(QSize(32, 32))

        self.verticalLayout_7.addWidget(self.parseWordFileExport_ParseButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.wordParseXls_page)
        self.configEdit_Page = QWidget()
        self.configEdit_Page.setObjectName(u"configEdit_Page")
        self.verticalLayout_15 = QVBoxLayout(self.configEdit_Page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.frame_2 = QFrame(self.configEdit_Page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.defaultDatabaseTypeName_label = QPushButton(self.frame_2)
        self.defaultDatabaseTypeName_label.setObjectName(u"defaultDatabaseTypeName_label")
        self.defaultDatabaseTypeName_label.setEnabled(False)
        self.defaultDatabaseTypeName_label.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/file_open/icons/icons8-sql-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultDatabaseTypeName_label.setIcon(icon16)

        self.verticalLayout_14.addWidget(self.defaultDatabaseTypeName_label)

        self.defaultDatabaseTypeConfig_ComboBox = QComboBox(self.frame_2)
        self.defaultDatabaseTypeConfig_ComboBox.addItem("")
        self.defaultDatabaseTypeConfig_ComboBox.setObjectName(u"defaultDatabaseTypeConfig_ComboBox")
        sizePolicy15.setHeightForWidth(self.defaultDatabaseTypeConfig_ComboBox.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseTypeConfig_ComboBox.setSizePolicy(sizePolicy15)
        self.defaultDatabaseTypeConfig_ComboBox.setEditable(False)

        self.verticalLayout_14.addWidget(self.defaultDatabaseTypeConfig_ComboBox)


        self.verticalLayout_15.addWidget(self.frame_2)

        self.line_9 = QFrame(self.configEdit_Page)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Raised)
        self.line_9.setLineWidth(20)
        self.line_9.setMidLineWidth(1)
        self.line_9.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_9)

        self.defaultDatabase_mainframe = QFrame(self.configEdit_Page)
        self.defaultDatabase_mainframe.setObjectName(u"defaultDatabase_mainframe")
        self.defaultDatabase_mainframe.setMaximumSize(QSize(16777215, 100))
        self.defaultDatabase_mainframe.setFrameShape(QFrame.StyledPanel)
        self.defaultDatabase_mainframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.defaultDatabase_mainframe)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.defaultDatabaseName_label = QPushButton(self.defaultDatabase_mainframe)
        self.defaultDatabaseName_label.setObjectName(u"defaultDatabaseName_label")
        self.defaultDatabaseName_label.setEnabled(False)
        self.defaultDatabaseName_label.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        self.defaultDatabaseName_label.setIcon(icon1)

        self.verticalLayout_16.addWidget(self.defaultDatabaseName_label)

        self.defaultDatabaseChoice_frame = QFrame(self.defaultDatabase_mainframe)
        self.defaultDatabaseChoice_frame.setObjectName(u"defaultDatabaseChoice_frame")
        self.defaultDatabaseChoice_frame.setFrameShape(QFrame.StyledPanel)
        self.defaultDatabaseChoice_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.defaultDatabaseChoice_frame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.defaultDatabaseConfig_ComboBox = QComboBox(self.defaultDatabaseChoice_frame)
        self.defaultDatabaseConfig_ComboBox.setObjectName(u"defaultDatabaseConfig_ComboBox")
        sizePolicy15.setHeightForWidth(self.defaultDatabaseConfig_ComboBox.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseConfig_ComboBox.setSizePolicy(sizePolicy15)
        self.defaultDatabaseConfig_ComboBox.setEditable(True)

        self.horizontalLayout_14.addWidget(self.defaultDatabaseConfig_ComboBox)

        self.defaultDatabaseCreate_Button = QPushButton(self.defaultDatabaseChoice_frame)
        self.defaultDatabaseCreate_Button.setObjectName(u"defaultDatabaseCreate_Button")
        sizePolicy7.setHeightForWidth(self.defaultDatabaseCreate_Button.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseCreate_Button.setSizePolicy(sizePolicy7)
        self.defaultDatabaseCreate_Button.setIcon(icon11)

        self.horizontalLayout_14.addWidget(self.defaultDatabaseCreate_Button)


        self.verticalLayout_16.addWidget(self.defaultDatabaseChoice_frame)


        self.verticalLayout_15.addWidget(self.defaultDatabase_mainframe)

        self.line_8 = QFrame(self.configEdit_Page)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Raised)
        self.line_8.setLineWidth(20)
        self.line_8.setMidLineWidth(1)
        self.line_8.setFrameShape(QFrame.HLine)

        self.verticalLayout_15.addWidget(self.line_8)

        self.defaultDatabaseCon_MainFrame = QFrame(self.configEdit_Page)
        self.defaultDatabaseCon_MainFrame.setObjectName(u"defaultDatabaseCon_MainFrame")
        self.defaultDatabaseCon_MainFrame.setMaximumSize(QSize(16777215, 16777215))
        self.defaultDatabaseCon_MainFrame.setFrameShape(QFrame.StyledPanel)
        self.defaultDatabaseCon_MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.defaultDatabaseCon_MainFrame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.defaultDatabaseConString_label_2 = QPushButton(self.defaultDatabaseCon_MainFrame)
        self.defaultDatabaseConString_label_2.setObjectName(u"defaultDatabaseConString_label_2")
        self.defaultDatabaseConString_label_2.setEnabled(False)
        self.defaultDatabaseConString_label_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgba(255,255,255,30); /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/file_open/icons/icons8-connection-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultDatabaseConString_label_2.setIcon(icon17)

        self.verticalLayout_17.addWidget(self.defaultDatabaseConString_label_2)

        self.defaultDatabaseConStringGen_Button = QPushButton(self.defaultDatabaseCon_MainFrame)
        self.defaultDatabaseConStringGen_Button.setObjectName(u"defaultDatabaseConStringGen_Button")
        sizePolicy7.setHeightForWidth(self.defaultDatabaseConStringGen_Button.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseConStringGen_Button.setSizePolicy(sizePolicy7)
        icon18 = QIcon()
        icon18.addFile(u":/file_open/icons/icons8-mechanistic-analysis-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultDatabaseConStringGen_Button.setIcon(icon18)

        self.verticalLayout_17.addWidget(self.defaultDatabaseConStringGen_Button)

        self.defaultDatabaseCon_frame_2 = QFrame(self.defaultDatabaseCon_MainFrame)
        self.defaultDatabaseCon_frame_2.setObjectName(u"defaultDatabaseCon_frame_2")
        self.defaultDatabaseCon_frame_2.setFrameShape(QFrame.StyledPanel)
        self.defaultDatabaseCon_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.defaultDatabaseCon_frame_2)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.defaultDatabaseConString_lineEdit_2 = QLineEdit(self.defaultDatabaseCon_frame_2)
        self.defaultDatabaseConString_lineEdit_2.setObjectName(u"defaultDatabaseConString_lineEdit_2")
        sizePolicy17 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy17.setHorizontalStretch(8)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.defaultDatabaseConString_lineEdit_2.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseConString_lineEdit_2.setSizePolicy(sizePolicy17)

        self.horizontalLayout_15.addWidget(self.defaultDatabaseConString_lineEdit_2)

        self.defaultDatabaseConTest_Button_2 = QPushButton(self.defaultDatabaseCon_frame_2)
        self.defaultDatabaseConTest_Button_2.setObjectName(u"defaultDatabaseConTest_Button_2")
        sizePolicy7.setHeightForWidth(self.defaultDatabaseConTest_Button_2.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseConTest_Button_2.setSizePolicy(sizePolicy7)
        icon19 = QIcon()
        icon19.addFile(u":/file_open/icons/icons8-wrench-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultDatabaseConTest_Button_2.setIcon(icon19)

        self.horizontalLayout_15.addWidget(self.defaultDatabaseConTest_Button_2)


        self.verticalLayout_17.addWidget(self.defaultDatabaseCon_frame_2)


        self.verticalLayout_15.addWidget(self.defaultDatabaseCon_MainFrame)

        self.defaultDatabaseConSave_Button = QPushButton(self.configEdit_Page)
        self.defaultDatabaseConSave_Button.setObjectName(u"defaultDatabaseConSave_Button")
        sizePolicy7.setHeightForWidth(self.defaultDatabaseConSave_Button.sizePolicy().hasHeightForWidth())
        self.defaultDatabaseConSave_Button.setSizePolicy(sizePolicy7)
        self.defaultDatabaseConSave_Button.setStyleSheet(u"QPushButton {\n"
"    background-color: #2C8F05; /* Steam's Button Background Color */\n"
"    color: #ffffff; /* White text for buttons */\n"
"    border: 1px solid #1b2838;\n"
"    border-radius: 12px;\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4B982C; /* Darker shade on hover */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #216407; /* Darker shade when pressed */\n"
"}")
        self.defaultDatabaseConSave_Button.setIcon(icon9)

        self.verticalLayout_15.addWidget(self.defaultDatabaseConSave_Button)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.configEdit_Page)

        self.horizontalLayout_11.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout_2.addWidget(self.frame)

        Parser_UI.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(Parser_UI)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 823, 22))
        Parser_UI.setMenuBar(self.menuBar)

        self.retranslateUi(Parser_UI)

        self.stackedWidget.setCurrentIndex(0)
        self.defaultDatabaseTypeConfig_ComboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Parser_UI)
    # setupUi

    def retranslateUi(self, Parser_UI):
        Parser_UI.setWindowTitle(QCoreApplication.translate("Parser_UI", u"Parser", None))
        self.actiontest3.setText(QCoreApplication.translate("Parser_UI", u"test3", None))
        self.actiontest4.setText(QCoreApplication.translate("Parser_UI", u"test4", None))
        self.label.setText(QCoreApplication.translate("Parser_UI", u"<html><head/><body><p>JParser v0.0.5</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.xlsRawImportPage_Button.setToolTip(QCoreApplication.translate("Parser_UI", u"Import raw excel file", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.xlsRawImportPage_Button.setWhatsThis(QCoreApplication.translate("Parser_UI", u"<html><head/><body><p>Import raw Excel file to Parse</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.xlsRawImportPage_Button.setText("")
#if QT_CONFIG(tooltip)
        self.databaseEdit_Button_2.setToolTip(QCoreApplication.translate("Parser_UI", u"Choose Parsed Excel File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.databaseEdit_Button_2.setWhatsThis(QCoreApplication.translate("Parser_UI", u"Database", None))
#endif // QT_CONFIG(whatsthis)
        self.databaseEdit_Button_2.setText("")
#if QT_CONFIG(tooltip)
        self.wordParsePage_Button.setToolTip(QCoreApplication.translate("Parser_UI", u"Parse Excel to Word Documents", None))
#endif // QT_CONFIG(tooltip)
        self.wordParsePage_Button.setText("")
#if QT_CONFIG(tooltip)
        self.settingsEdit_Button.setToolTip(QCoreApplication.translate("Parser_UI", u"Choose Parsed Excel File", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.settingsEdit_Button.setWhatsThis(QCoreApplication.translate("Parser_UI", u"Config", None))
#endif // QT_CONFIG(whatsthis)
        self.settingsEdit_Button.setText("")
#if QT_CONFIG(tooltip)
        self.exit_Button.setToolTip(QCoreApplication.translate("Parser_UI", u"Exit from program", None))
#endif // QT_CONFIG(tooltip)
        self.exit_Button.setText("")
        self.xlsRawFileImport_LabelButton.setText(QCoreApplication.translate("Parser_UI", u"Raw Excel File Import", None))
        self.xlsRawFilePath_Line.setText("")
        self.xlsRawFilePath_Line.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Click browse to find xls File", None))
        self.xlsRawFilePathBrowse_Button.setText(QCoreApplication.translate("Parser_UI", u"Browse", None))
        self.xlsRawFilePathLoad_Button.setText(QCoreApplication.translate("Parser_UI", u"Load", None))
        self.coulumnChoose_LabelButton.setText(QCoreApplication.translate("Parser_UI", u"Choose Column of ID", None))
        self.databaseBrowse_LabelButton.setText(QCoreApplication.translate("Parser_UI", u"Database Dictionary Load", None))
        self.DatabaseChoice_ComboBox.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Choose a DataBase, then click connect", None))
        self.DatabaseConnect_Button.setText(QCoreApplication.translate("Parser_UI", u"Connect", None))
        self.TableChoice_ComboBox.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Choose a Table", None))
        self.DatabaseConnectionSave_Button.setText(QCoreApplication.translate("Parser_UI", u"Save", None))
        self.databaseEdit_Button.setText(QCoreApplication.translate("Parser_UI", u"Edit DataBase", None))
        self.xlsParsedFilePath_Line.setText("")
        self.xlsParsedFilePath_Line.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Where to save Excel File", None))
        self.xlsParsedFilePathBrowse_Button.setText(QCoreApplication.translate("Parser_UI", u"Browse", None))
        self.parseToXlsFile_Button.setText(QCoreApplication.translate("Parser_UI", u"Parse to xls file", None))
        self.databaseEdit_label.setText(QCoreApplication.translate("Parser_UI", u"Database Edit", None))
        self.DatabaseChoice_ComboBox_2.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Choose a DataBase, then click connect", None))
        self.DatabaseConnect_Button_2.setText(QCoreApplication.translate("Parser_UI", u"Connect", None))
        self.DatabaseCreate_Button.setText(QCoreApplication.translate("Parser_UI", u"Create", None))
        self.TableChoice_ComboBox_2.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Choose a Table", None))
        self.DatabaseConnectionSave_Button_2.setText(QCoreApplication.translate("Parser_UI", u"Save", None))
        self.tableCreate_Button.setText(QCoreApplication.translate("Parser_UI", u"Create", None))
        self.databaseReOrder_Button.setText(QCoreApplication.translate("Parser_UI", u"Re-order Records", None))
        self.databaseRegenID_Button.setText(QCoreApplication.translate("Parser_UI", u"Regenerate ID", None))
        self.xlsParsedFileImport_LabelButton.setText(QCoreApplication.translate("Parser_UI", u"Excel File Import", None))
        self.xlsParsedFileImport_Line.setText("")
        self.xlsParsedFileImport_Line.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Click browse to find Excel File", None))
        self.xlsParsedFileImportBrowse_Button.setText(QCoreApplication.translate("Parser_UI", u"Browse", None))
        self.templateWordImport_LabelButton.setText(QCoreApplication.translate("Parser_UI", u"Word Template Import", None))
        self.templateWordImport_Line.setText("")
        self.templateWordImport_Line.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Click browse to find Word Template File", None))
        self.templateWordImport_Button.setText(QCoreApplication.translate("Parser_UI", u"Browse", None))
        self.parseWordFileExport_LabelButton.setText(QCoreApplication.translate("Parser_UI", u"Word File Export", None))
        self.parseEveryXlsRow_CheckBox.setText(QCoreApplication.translate("Parser_UI", u"Create Document for every row in excel file?", None))
        self.parseWordFileExport_Line.setText("")
        self.parseWordFileExport_Line.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Click browse to set Word File", None))
        self.parseWordFileExport_Button.setText(QCoreApplication.translate("Parser_UI", u"Browse", None))
        self.parseWordFileExport_ParseButton.setText(QCoreApplication.translate("Parser_UI", u"Parse", None))
        self.defaultDatabaseTypeName_label.setText(QCoreApplication.translate("Parser_UI", u"Database Type", None))
        self.defaultDatabaseTypeConfig_ComboBox.setItemText(0, QCoreApplication.translate("Parser_UI", u"sqlite3", None))

        self.defaultDatabaseTypeConfig_ComboBox.setCurrentText(QCoreApplication.translate("Parser_UI", u"sqlite3", None))
        self.defaultDatabaseTypeConfig_ComboBox.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Choose a DataBase, then click connect", None))
        self.defaultDatabaseName_label.setText(QCoreApplication.translate("Parser_UI", u"Default Database", None))
        self.defaultDatabaseConfig_ComboBox.setPlaceholderText(QCoreApplication.translate("Parser_UI", u"Choose a DataBase, then click connect", None))
        self.defaultDatabaseCreate_Button.setText(QCoreApplication.translate("Parser_UI", u"Create", None))
        self.defaultDatabaseConString_label_2.setText(QCoreApplication.translate("Parser_UI", u"Connection String", None))
        self.defaultDatabaseConStringGen_Button.setText(QCoreApplication.translate("Parser_UI", u"Generate Connection String", None))
        self.defaultDatabaseConTest_Button_2.setText(QCoreApplication.translate("Parser_UI", u"Test", None))
        self.defaultDatabaseConSave_Button.setText(QCoreApplication.translate("Parser_UI", u"Save Config", None))
    # retranslateUi

