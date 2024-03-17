import json
import shutil
from pathlib import Path
import PyInstaller.__main__
import pyinstaller_versionfile


class Builder:
    def __init__(self, app_path: Path, app_name: str, app_desc: str, icon_path: Path, version: str, files_to_copy=None,
                 dirs_to_copy=None):
        if files_to_copy is None:
            files_to_copy = []
        if dirs_to_copy is None:
            dirs_to_copy = []

        self.__app_path = app_path
        self.__app_name = app_name
        self.__app_desc = app_desc
        self.__files_to_copy = files_to_copy
        self.__dirs_to_copy = dirs_to_copy
        self.__icon_path = icon_path
        self.__version = version

    @staticmethod
    def __testing():
        ...

    def __prepare_file_system(self):
        if self.__app_path.exists():
            shutil.rmtree(self.__app_path)
        self.__app_path.mkdir()
        for directory in self.__dirs_to_copy:
            shutil.copytree(Path().absolute().joinpath(directory), self.__app_path.joinpath(directory))

    def __build(self):
        pyinstaller_versionfile.create_versionfile(
            output_file="versionfile.txt",
            version=f"{self.__version}",
            company_name="Rodion Shevchenko",
            file_description=f'{self.__app_desc}',
            internal_name="Simple App",
            legal_copyright="© Rodion Chevchenko. All rights reserved.",
            original_filename=f'{self.__app_name}.exe',
            product_name=f'{self.__app_name}'
        )

        PyInstaller.__main__.run([
            '--onefile',
            '--add-data=C:/Users/Asus/PycharmProjects/Excell_addIn_Installer/venv/Lib/site-packages/grapheme/data/grapheme_break_property.json;/grapheme/data',
            '--noupx',
            '-c',
            f'--icon={self.__icon_path.relative_to((Path().absolute()))}',
            f'--distpath={str(self.__app_path)}',
            f'-n{self.__app_name.strip()}',
            'main.py',
            '--version-file=versionfile.txt'
        ])

    def __merge(self):
        self.__prepare_file_system()
        self.__build()

    def start_merge(self):
        self.__merge()


def main():
    app_path = Path(Path().absolute() / "app_EXE").resolve()
    app_name = 'Parser'
    app_desc = 'xls_word_parser'
    app_icon_path = Path().absolute().joinpath('icon/file.ico')
    app_version = '0.0.1'
    dirs_to_copy = []
    app_builder = Builder(
        app_path=app_path,
        app_name=app_name,
        app_desc=app_desc,
        icon_path=app_icon_path,
        version=app_version,
        dirs_to_copy=dirs_to_copy
    )
    app_builder.start_merge()


if __name__ == '__main__':
    main()
