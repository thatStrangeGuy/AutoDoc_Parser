import sys
from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox

from UI.base_qt_ui import icons_rc


def show_exit_dialog():
    msgbox = QMessageBox()
    msgbox.setWindowTitle("Exit")
    icon = msgbox.Icon.Information
    msgbox.setIcon(icon)
    title_icon = QIcon()
    title_icon.addFile(u":/file_open/icons/icons8-exit-80_RED.png", QSize(), QIcon.Normal, QIcon.Off)
    msgbox.setWindowIcon(title_icon)

    with open(Path().absolute().joinpath('UI', 'style_main.css'), 'r') as style_file:
        style = style_file.read()
        msgbox.setStyleSheet(style)

    msgbox.setText("Are you sure to exit?")
    accept = msgbox.addButton("Yes", QMessageBox.ButtonRole.AcceptRole)
    reject = msgbox.addButton("No", QMessageBox.ButtonRole.RejectRole)
    msgbox.exec()
    if msgbox.clickedButton() == accept:
        sys.exit(0)
    elif msgbox.clickedButton() == reject:
        msgbox.close()


def show_error_message(msg):
    msgbox = QMessageBox()
    msgbox.setWindowTitle("Error!")
    icon = msgbox.Icon.Critical
    msgbox.setIcon(icon)
    title_icon = QIcon()
    title_icon.addFile(u":/file_open/icons/icons8-error-64.png", QSize(), QIcon.Normal, QIcon.Off)
    msgbox.setWindowIcon(title_icon)

    with open(Path().absolute().joinpath('UI', 'style_main.css'), 'r') as style_file:
        style = style_file.read()
        style += '''\nQLabel{min-width:200 px; font-size: 12px;text-align:left;} QPushButton{ width:100px; font-size: 16px; }'''
        msgbox.setStyleSheet(style)

    msgbox.setText(f"OOPS!Something went wrong!")
    msgbox.setDetailedText(f"Error!\n\n{msg}")
    accept = msgbox.addButton("Ok", QMessageBox.ButtonRole.YesRole)
    msgbox.exec()
    if msgbox.clickedButton() == accept:
        msgbox.close()
