import os, re
import time
from pathlib import Path

import os
from pathlib import Path


def generate_all_ui2py(path: Path | str = Path().absolute()):
    if isinstance(path, str):
        path = Path(path)
    ui_file_paths = list(path.glob("*.ui"))
    rc_file_paths = list(path.glob("**/*.qrc"))

    for i in rc_file_paths:
        cmd_rc = f'pyside6-rcc {i.absolute()} > {path.absolute().joinpath(i.stem)}_rc.py'
        os.system(cmd_rc)

    for i in ui_file_paths:
        cmd_ui = f'pyside6-uic {i.absolute()} > {path.absolute().joinpath(i.stem)}.py'
        os.system(cmd_ui)

    for i in rc_file_paths:
        for j in ui_file_paths:
            py_file_path = path.joinpath(j.stem + ".py")
            if not py_file_path.exists():
                print(f"Python file {py_file_path} does not exist. Skipping...")
                continue

            with open(py_file_path, "r") as py_file:
                py_content = py_file.read()

            replaced_content = py_content.replace(f"import {i.stem}_rc", f"from UI.base_qt_ui import {i.stem}_rc")

            with open(py_file_path, "w") as py_file:
                py_file.write(replaced_content)

            print(f"Updated {py_file_path} successfully.")


if __name__ == '__main__':
    generate_all_ui2py()
