import logging
from pathlib import Path
import yaml

default_config = dict()

default_config["db_dir"] = str(Path().absolute().joinpath("db"))
default_config["db_name"] = "default"
default_config["db_type"] = "sqlite"
default_config["db_path"] = str(Path(default_config.get('db_dir')).joinpath(f'{default_config["db_name"]}.db'))
default_config["conn_str"] = f'sqlite:////{default_config["db_path"]}'
default_config["index_types"] = ["Number", "Array"]
default_config["value_types"] = ["Number", "String"]

logger = logging.getLogger('app.config_controller')


def read_config(file_path):
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def write_config(file_path, config):
    with open(file_path, 'w') as file:
        yaml.dump(config, file)


def restore_default_config():
    try:
        write_config('config.yaml', default_config)
        return ["Succesfull", None]
    except Exception as _ex:
        logger.critical(_ex)
        return [None, _ex]
