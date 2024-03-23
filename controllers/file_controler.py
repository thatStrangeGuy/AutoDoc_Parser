from pathlib import Path

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QDialog


def browse_filepath(defaultDir=QDir.currentPath(), filter='All Files (*)', title="Browse", setmode=QFileDialog.FileMode.AnyFile):
    FileDialog = QFileDialog()
    FileDialog.setFileMode(setmode)
    file, _ = FileDialog.getOpenFileName(None, title, dir=defaultDir, filter=filter)
    return Path(file).absolute()
