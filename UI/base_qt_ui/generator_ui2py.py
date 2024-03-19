import os, re
from pathlib import Path


def generate_all_ui2py(path: Path | str = Path().absolute()):
    if isinstance(path, str):
        path = Path(path)
    ui_file_paths = path.glob("*.ui")
    rc_file_paths = path.glob("**/*.qrc")
    for i in ui_file_paths:
        cmd_ui = f'pyside6-uic {i.absolute()} > {path.absolute().joinpath(i.stem)}.py'
        os.popen(cmd_ui)
    for i in rc_file_paths:
        cmd_rc = f'pyside6-rcc {i.absolute()} > {path.absolute().joinpath(i.stem)}_rc.py'
        os.popen(cmd_rc)


if __name__ == '__main__':
    generate_all_ui2py()
