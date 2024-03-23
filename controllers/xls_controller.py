import logging
from pathlib import Path

import pandas

logger = logging.getLogger('app.xls_controller')


def excel_to_dataframe(path_file: Path | str):
    try:
        if isinstance(path_file, Path):
            path_file = str(path_file)
        df = pandas.read_excel(path_file)
        return df
    except FileNotFoundError as _ex:
        logger.critical(f"Error: File not found: {_ex}")
        raise FileNotFoundError


def get_columns(path_file):
    try:
        df = excel_to_dataframe(path_file)
        return df.columns.tolist()
    except FileNotFoundError:
        raise FileNotFoundError
