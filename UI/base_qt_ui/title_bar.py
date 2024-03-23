# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'title_bar.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from UI.base_qt_ui import icons_rc

class Ui_TitleBar(object):
    def setupUi(self, TitleBar):
        if not TitleBar.objectName():
            TitleBar.setObjectName(u"TitleBar")
        TitleBar.resize(967, 64)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TitleBar.sizePolicy().hasHeightForWidth())
        TitleBar.setSizePolicy(sizePolicy)
        TitleBar.setStyleSheet(u"QWidget {\n"
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
        self.verticalLayout = QVBoxLayout(TitleBar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.titlebar_frame = QFrame(TitleBar)
        self.titlebar_frame.setObjectName(u"titlebar_frame")
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
        self.label.setMinimumSize(QSize(0, 0))
        self.label.setMaximumSize(QSize(776, 283))
        self.label.setStyleSheet(u"")
        self.label.setTextFormat(Qt.RichText)
        self.label.setScaledContents(False)

        self.horizontalLayout.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_minimize = QPushButton(self.titlebar_frame)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.titlebar_frame)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        self.btn_maximize_restore.setMaximumSize(QSize(16, 16))

        self.horizontalLayout.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.titlebar_frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMaximumSize(QSize(16, 16))
        self.btn_close.setStyleSheet(u"")

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.titlebar_frame)


        self.retranslateUi(TitleBar)

        QMetaObject.connectSlotsByName(TitleBar)
    # setupUi

    def retranslateUi(self, TitleBar):
        TitleBar.setWindowTitle(QCoreApplication.translate("TitleBar", u"Form", None))
        self.label.setText(QCoreApplication.translate("TitleBar", u"<html><head/><body><p>JParser v0.0.5</p></body></html>", None))
        self.btn_minimize.setText("")
        self.btn_maximize_restore.setText("")
        self.btn_close.setText("")
    # retranslateUi

