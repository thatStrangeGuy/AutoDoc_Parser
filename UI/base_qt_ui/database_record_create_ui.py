# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'database_record_create_ui.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)
from UI.base_qt_ui import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(946, 152)
        Form.setMaximumSize(QSize(16777215, 16777215))
        Form.setStyleSheet(u"QWidget {\n"
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
"QSpinBox {\n"
"    color: #c6d4df; /* Text color */\n"
"    background-color: #1c2735; /* Background color */\n"
"    border: 1px solid #5a90d8; /* Border color */\n"
"    padding: 2px 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    background-color: #7289da; /* Button background color */\n"
"    border: 1px solid #7289da; /* Button border color */\n"
"    border-radius: 4px;\n"
"    width: 15px;\n"
"}\n"
"\n"
"QSpinBox::up-button:hover, QSpinBox::down-button:hover {\n"
"    background-color: #677bc4; /* Darker shade on hover */\n"
"}\n"
"\n"
"QSpinBox::up-button:pressed, QSpinBox::down-button:pressed {\n"
"    background-color: #5865a6; /* Darker shade when pressed */\n"
"}\n"
"\n"
"QSpinBox::up-arrow, QSpinBox::down-arrow {\n"
"    color: #c6d4df; /* Arrow color */\n"
"    font-size: 10"
                        "px; /* Arrow size */\n"
"}\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_9 = QFrame(Form)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 100))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_9)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.databaseRecordID_frame = QFrame(self.frame_9)
        self.databaseRecordID_frame.setObjectName(u"databaseRecordID_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.databaseRecordID_frame.sizePolicy().hasHeightForWidth())
        self.databaseRecordID_frame.setSizePolicy(sizePolicy)
        self.databaseRecordID_frame.setStyleSheet(u"")
        self.databaseRecordID_frame.setFrameShape(QFrame.StyledPanel)
        self.databaseRecordID_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.databaseRecordID_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.databaseRecordID_Label = QLabel(self.databaseRecordID_frame)
        self.databaseRecordID_Label.setObjectName(u"databaseRecordID_Label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.databaseRecordID_Label.sizePolicy().hasHeightForWidth())
        self.databaseRecordID_Label.setSizePolicy(sizePolicy1)
        self.databaseRecordID_Label.setTextFormat(Qt.AutoText)
        self.databaseRecordID_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.databaseRecordID_Label)

        self.databaseRecordID_Line = QLineEdit(self.databaseRecordID_frame)
        self.databaseRecordID_Line.setObjectName(u"databaseRecordID_Line")
        self.databaseRecordID_Line.setEnabled(False)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(2)
        sizePolicy2.setHeightForWidth(self.databaseRecordID_Line.sizePolicy().hasHeightForWidth())
        self.databaseRecordID_Line.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.databaseRecordID_Line)


        self.horizontalLayout.addWidget(self.databaseRecordID_frame)

        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.databaseRecordName_Label = QLabel(self.frame_10)
        self.databaseRecordName_Label.setObjectName(u"databaseRecordName_Label")
        sizePolicy1.setHeightForWidth(self.databaseRecordName_Label.sizePolicy().hasHeightForWidth())
        self.databaseRecordName_Label.setSizePolicy(sizePolicy1)
        self.databaseRecordName_Label.setTextFormat(Qt.AutoText)
        self.databaseRecordName_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.databaseRecordName_Label)

        self.databaseRecordName_Line = QLineEdit(self.frame_10)
        self.databaseRecordName_Line.setObjectName(u"databaseRecordName_Line")
        sizePolicy2.setHeightForWidth(self.databaseRecordName_Line.sizePolicy().hasHeightForWidth())
        self.databaseRecordName_Line.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.databaseRecordName_Line)


        self.horizontalLayout.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_9)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy3)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.databaseRecordIndType_Label = QLabel(self.frame_11)
        self.databaseRecordIndType_Label.setObjectName(u"databaseRecordIndType_Label")
        sizePolicy1.setHeightForWidth(self.databaseRecordIndType_Label.sizePolicy().hasHeightForWidth())
        self.databaseRecordIndType_Label.setSizePolicy(sizePolicy1)
        self.databaseRecordIndType_Label.setTextFormat(Qt.AutoText)
        self.databaseRecordIndType_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.databaseRecordIndType_Label)

        self.databaseRecordIndType_ComboBox = QComboBox(self.frame_11)
        self.databaseRecordIndType_ComboBox.addItem("")
        self.databaseRecordIndType_ComboBox.addItem("")
        self.databaseRecordIndType_ComboBox.setObjectName(u"databaseRecordIndType_ComboBox")
        sizePolicy2.setHeightForWidth(self.databaseRecordIndType_ComboBox.sizePolicy().hasHeightForWidth())
        self.databaseRecordIndType_ComboBox.setSizePolicy(sizePolicy2)

        self.verticalLayout_10.addWidget(self.databaseRecordIndType_ComboBox)


        self.horizontalLayout.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_9)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_12)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.databaseRecordIndex_Label = QLabel(self.frame_12)
        self.databaseRecordIndex_Label.setObjectName(u"databaseRecordIndex_Label")
        sizePolicy1.setHeightForWidth(self.databaseRecordIndex_Label.sizePolicy().hasHeightForWidth())
        self.databaseRecordIndex_Label.setSizePolicy(sizePolicy1)
        self.databaseRecordIndex_Label.setTextFormat(Qt.AutoText)
        self.databaseRecordIndex_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.databaseRecordIndex_Label)

        self.databaseRecordIndex_lineEdit = QLineEdit(self.frame_12)
        self.databaseRecordIndex_lineEdit.setObjectName(u"databaseRecordIndex_lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(1)
        sizePolicy4.setVerticalStretch(2)
        sizePolicy4.setHeightForWidth(self.databaseRecordIndex_lineEdit.sizePolicy().hasHeightForWidth())
        self.databaseRecordIndex_lineEdit.setSizePolicy(sizePolicy4)

        self.verticalLayout_11.addWidget(self.databaseRecordIndex_lineEdit)


        self.horizontalLayout.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_9)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.databaseRecordColumn_label = QLabel(self.frame_13)
        self.databaseRecordColumn_label.setObjectName(u"databaseRecordColumn_label")
        sizePolicy1.setHeightForWidth(self.databaseRecordColumn_label.sizePolicy().hasHeightForWidth())
        self.databaseRecordColumn_label.setSizePolicy(sizePolicy1)
        self.databaseRecordColumn_label.setTextFormat(Qt.AutoText)
        self.databaseRecordColumn_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.databaseRecordColumn_label)

        self.databaseRecordColumn_lineEdit = QLineEdit(self.frame_13)
        self.databaseRecordColumn_lineEdit.setObjectName(u"databaseRecordColumn_lineEdit")
        sizePolicy4.setHeightForWidth(self.databaseRecordColumn_lineEdit.sizePolicy().hasHeightForWidth())
        self.databaseRecordColumn_lineEdit.setSizePolicy(sizePolicy4)

        self.verticalLayout_12.addWidget(self.databaseRecordColumn_lineEdit)


        self.horizontalLayout.addWidget(self.frame_13)

        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_14)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.databaseRecordKey_label = QLabel(self.frame_14)
        self.databaseRecordKey_label.setObjectName(u"databaseRecordKey_label")
        sizePolicy1.setHeightForWidth(self.databaseRecordKey_label.sizePolicy().hasHeightForWidth())
        self.databaseRecordKey_label.setSizePolicy(sizePolicy1)
        self.databaseRecordKey_label.setTextFormat(Qt.AutoText)
        self.databaseRecordKey_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.databaseRecordKey_label)

        self.databaseRecordKey_lineEdit = QLineEdit(self.frame_14)
        self.databaseRecordKey_lineEdit.setObjectName(u"databaseRecordKey_lineEdit")
        sizePolicy2.setHeightForWidth(self.databaseRecordKey_lineEdit.sizePolicy().hasHeightForWidth())
        self.databaseRecordKey_lineEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_13.addWidget(self.databaseRecordKey_lineEdit)


        self.horizontalLayout.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_9)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy3.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy3)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_15)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.databaseRecordValType_label = QLabel(self.frame_15)
        self.databaseRecordValType_label.setObjectName(u"databaseRecordValType_label")
        sizePolicy1.setHeightForWidth(self.databaseRecordValType_label.sizePolicy().hasHeightForWidth())
        self.databaseRecordValType_label.setSizePolicy(sizePolicy1)
        self.databaseRecordValType_label.setTextFormat(Qt.AutoText)
        self.databaseRecordValType_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.databaseRecordValType_label)

        self.databaseRecordValType_comboBox = QComboBox(self.frame_15)
        self.databaseRecordValType_comboBox.addItem("")
        self.databaseRecordValType_comboBox.addItem("")
        self.databaseRecordValType_comboBox.setObjectName(u"databaseRecordValType_comboBox")
        sizePolicy2.setHeightForWidth(self.databaseRecordValType_comboBox.sizePolicy().hasHeightForWidth())
        self.databaseRecordValType_comboBox.setSizePolicy(sizePolicy2)

        self.verticalLayout_14.addWidget(self.databaseRecordValType_comboBox)


        self.horizontalLayout.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.frame_9)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_16)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.databaseRecordValue_label = QLabel(self.frame_16)
        self.databaseRecordValue_label.setObjectName(u"databaseRecordValue_label")
        sizePolicy1.setHeightForWidth(self.databaseRecordValue_label.sizePolicy().hasHeightForWidth())
        self.databaseRecordValue_label.setSizePolicy(sizePolicy1)
        self.databaseRecordValue_label.setTextFormat(Qt.AutoText)
        self.databaseRecordValue_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.databaseRecordValue_label)

        self.databaseRecordValue_lineEdit = QLineEdit(self.frame_16)
        self.databaseRecordValue_lineEdit.setObjectName(u"databaseRecordValue_lineEdit")
        sizePolicy2.setHeightForWidth(self.databaseRecordValue_lineEdit.sizePolicy().hasHeightForWidth())
        self.databaseRecordValue_lineEdit.setSizePolicy(sizePolicy2)

        self.verticalLayout_15.addWidget(self.databaseRecordValue_lineEdit)


        self.horizontalLayout.addWidget(self.frame_16)

        self.databaseRecordOrderID_frame = QFrame(self.frame_9)
        self.databaseRecordOrderID_frame.setObjectName(u"databaseRecordOrderID_frame")
        sizePolicy.setHeightForWidth(self.databaseRecordOrderID_frame.sizePolicy().hasHeightForWidth())
        self.databaseRecordOrderID_frame.setSizePolicy(sizePolicy)
        self.databaseRecordOrderID_frame.setStyleSheet(u"")
        self.databaseRecordOrderID_frame.setFrameShape(QFrame.StyledPanel)
        self.databaseRecordOrderID_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.databaseRecordOrderID_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.databaseRecordOrderID_Label = QLabel(self.databaseRecordOrderID_frame)
        self.databaseRecordOrderID_Label.setObjectName(u"databaseRecordOrderID_Label")
        sizePolicy1.setHeightForWidth(self.databaseRecordOrderID_Label.sizePolicy().hasHeightForWidth())
        self.databaseRecordOrderID_Label.setSizePolicy(sizePolicy1)
        self.databaseRecordOrderID_Label.setTextFormat(Qt.AutoText)
        self.databaseRecordOrderID_Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.databaseRecordOrderID_Label)

        self.databaseRecordOrderID_spinBox = QSpinBox(self.databaseRecordOrderID_frame)
        self.databaseRecordOrderID_spinBox.setObjectName(u"databaseRecordOrderID_spinBox")

        self.verticalLayout_4.addWidget(self.databaseRecordOrderID_spinBox)


        self.horizontalLayout.addWidget(self.databaseRecordOrderID_frame)

        self.frame = QFrame(self.frame_9)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.databaseRecordDelete_Button = QPushButton(self.frame)
        self.databaseRecordDelete_Button.setObjectName(u"databaseRecordDelete_Button")
        icon = QIcon()
        icon.addFile(u":/file_open/icons/icons8-delete-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseRecordDelete_Button.setIcon(icon)

        self.verticalLayout_3.addWidget(self.databaseRecordDelete_Button)

        self.databaseRecordSave_Button = QPushButton(self.frame)
        self.databaseRecordSave_Button.setObjectName(u"databaseRecordSave_Button")
        icon1 = QIcon()
        icon1.addFile(u":/file_open/icons/icons8-save-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseRecordSave_Button.setIcon(icon1)

        self.verticalLayout_3.addWidget(self.databaseRecordSave_Button)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frame_9)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.databaseRecordUpperOrder_Button = QPushButton(self.frame_2)
        self.databaseRecordUpperOrder_Button.setObjectName(u"databaseRecordUpperOrder_Button")
        icon2 = QIcon()
        icon2.addFile(u":/file_open/icons/icons8-up-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseRecordUpperOrder_Button.setIcon(icon2)

        self.verticalLayout_5.addWidget(self.databaseRecordUpperOrder_Button)

        self.databaseRecordDownOrder_Button = QPushButton(self.frame_2)
        self.databaseRecordDownOrder_Button.setObjectName(u"databaseRecordDownOrder_Button")
        icon3 = QIcon()
        icon3.addFile(u":/file_open/icons/icons8-down-90.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseRecordDownOrder_Button.setIcon(icon3)

        self.verticalLayout_5.addWidget(self.databaseRecordDownOrder_Button)


        self.horizontalLayout.addWidget(self.frame_2)


        self.verticalLayout.addWidget(self.frame_9)

        self.databaseRecordCreate_Button = QPushButton(Form)
        self.databaseRecordCreate_Button.setObjectName(u"databaseRecordCreate_Button")
        icon4 = QIcon()
        icon4.addFile(u":/file_open/icons/icons8-add-database-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.databaseRecordCreate_Button.setIcon(icon4)

        self.verticalLayout.addWidget(self.databaseRecordCreate_Button)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.databaseRecordID_Label.setText(QCoreApplication.translate("Form", u"ID", None))
        self.databaseRecordName_Label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.databaseRecordIndType_Label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">Index type</span></p></body></html>", None))
        self.databaseRecordIndType_ComboBox.setItemText(0, QCoreApplication.translate("Form", u"Number", None))
        self.databaseRecordIndType_ComboBox.setItemText(1, QCoreApplication.translate("Form", u"Array", None))

        self.databaseRecordIndex_Label.setText(QCoreApplication.translate("Form", u"Index", None))
        self.databaseRecordColumn_label.setText(QCoreApplication.translate("Form", u"Column", None))
        self.databaseRecordKey_label.setText(QCoreApplication.translate("Form", u"Key", None))
        self.databaseRecordValType_label.setText(QCoreApplication.translate("Form", u"Value Type", None))
        self.databaseRecordValType_comboBox.setItemText(0, QCoreApplication.translate("Form", u"String", None))
        self.databaseRecordValType_comboBox.setItemText(1, QCoreApplication.translate("Form", u"Number", None))

        self.databaseRecordValue_label.setText(QCoreApplication.translate("Form", u"Value", None))
        self.databaseRecordOrderID_Label.setText(QCoreApplication.translate("Form", u"Order ID", None))
        self.databaseRecordDelete_Button.setText("")
        self.databaseRecordSave_Button.setText("")
        self.databaseRecordUpperOrder_Button.setText("")
        self.databaseRecordDownOrder_Button.setText("")
        self.databaseRecordCreate_Button.setText(QCoreApplication.translate("Form", u"Create Record", None))
    # retranslateUi

