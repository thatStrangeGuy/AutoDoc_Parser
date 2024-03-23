import os, re
import time
from pathlib import Path


def generate_all_ui2py(path: Path | str = Path().absolute()):
    if isinstance(path, str):
        path = Path(path)
    ui_file_paths = list(path.glob("*.ui"))
    rc_file_paths = list(path.glob("**/*.qrc"))
    for i in rc_file_paths:
        cmd_rc = f'pyside6-rcc {i.absolute()} > {path.absolute().joinpath(i.stem)}_rc.py'
        os.popen(cmd_rc)
    for i in ui_file_paths:
        cmd_ui = f'pyside6-uic {i.absolute()} > {path.absolute().joinpath(i.stem)}.py'
        os.popen(cmd_ui)

    for numi, i in enumerate(rc_file_paths):
        print(
            f"Starting with rc files{i.stem}: {numi + 1}/{len(rc_file_paths)} --- {numi / len(rc_file_paths) * 100} % ")
        for numj, j in enumerate(ui_file_paths):
            print(
                f"Working with UI file: {j.stem}: {numj + 1} / {len(ui_file_paths)}  --- {numj / len(ui_file_paths) * 100} %")
            with open(f"{j.parent.absolute().joinpath(j.stem)}.py", "r") as rc_file:
                temp_file = rc_file.read()
            test = temp_file.replace(f"import {i.stem}_rc",
                                     f"from UI.base_qt_ui import {i.stem}_rc")
            time.sleep(0.5)
            try:
                with open(f"{j.parent.absolute().joinpath(j.stem)}.py", "w") as ui_file:
                    ui_file.write(test)
            except PermissionError:
                print("File didnt closed so fast, retry...")
                time.sleep(3)
                with open(f"{j.parent.absolute().joinpath(j.stem)}.py", "w") as ui_file:
                    ui_file.write(test)


if __name__ == '__main__':
    generate_all_ui2py()
