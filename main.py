from PySide6.QtWidgets import QApplication
import sys

from UI.MainWindow import MainWindow


def main():
    app = QApplication()
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
