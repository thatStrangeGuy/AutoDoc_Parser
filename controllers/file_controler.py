import datetime
import logging
from pathlib import Path

from PySide6.QtCore import QDir
from PySide6.QtWidgets import QFileDialog
from PySide6.QtWidgets import QDialog

logger = logging.getLogger("app.file_controller")


def browse_filepath(defaultDir=QDir.currentPath(), filter='All Files (*)', title="Browse",
                    setmode=QFileDialog.FileMode.AnyFile):
    FileDialog = QFileDialog()
    FileDialog.setFileMode(setmode)
    file, _ = FileDialog.getOpenFileName(None, title, dir=defaultDir, filter=filter)
    return Path(file).absolute()


def check_filepath(path: str | Path, ext: list):
    try:
        path = Path(path).absolute()
        if not path.exists():
            raise FileNotFoundError(f"Path {path} not exists!")
        if path.is_dir():
            raise TypeError(f"File {path} is a directory, need a file of extentions\n{','.join(ext)}")
        if path.suffix not in ext:
            raise TypeError(f"File {str(path)} has type of {path.suffix}\nExpected {','.join(ext)}")
        return [Path(path).absolute(), None]
    except Exception as _ex:
        DT = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        logger.critical(f"FIlePath {path} not found or has errors!Error\n{_ex}")
        return [None, f"Something wrong with filepath!Error:\n{_ex}\n\nTime: {DT}"]


def check_dirpath(path: str | Path):
    try:
        path = Path(path).absolute()
        if not path.exists():
            raise FileNotFoundError(f"Path {path} not exists!")
        if not path.is_dir():
            raise TypeError(f"File {path} is not a directory!")
        return [Path(path).absolute(), None]
    except Exception as _ex:
        DT = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        logger.critical(f"Path {path} not found or has errors!Error\n{_ex}")
        return [None, f"Something wrong with Path!Error:\n{_ex}\n\nTime: {DT}"]


def check_filepath_nonExist(path: str | Path, ext: list):
    try:
        path = Path(path).absolute()
        if path.exists():
            raise FileNotFoundError(f"Path {path} already exists!")
        if path.is_dir():
            raise TypeError(f"File {path} is a directory, need a file of extentions\n{','.join(ext)}")
        if path.suffix not in ext:
            raise TypeError(f"File {str(path)} has type of {path.suffix}\nExpected {','.join(ext)}")
        return [Path(path).absolute(), None]
    except Exception as _ex:
        DT = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        logger.critical(f"FIlePath {path} not found or has errors!Error\n{_ex}")
        return [None, f"Something wrong with filepath!Error:\n{_ex}\n\nTime: {DT}"]
