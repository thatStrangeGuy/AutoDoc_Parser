# TODO: Writing Connection to sqlite, handling connections, functions for creating methods, also checking databases
import logging
from pathlib import Path
from controllers import config_controller

from controllers import file_controler

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.models import IndexType, ValueType, Base, Dictionary

config = config_controller.read_config("config.yaml")

logger = logging.getLogger("app.db_controller")


def get_sqlite_databases(db_dir: str | Path):
    path, error = file_controler.check_dirpath(Path(db_dir))
    if path is None:
        return [None, error]
    else:
        databases = list(Path(path).glob('*.db'))
        return [databases, None]


def CreateDatabase(database_path: str | Path):
    try:
        database_url = f"sqlite:///{Path(database_path).resolve()}"
        # Create the engine
        engine = create_engine(database_url)
        Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create default IndexType records
        index_types = []
        for i in config['index_types']:
            index_type = {"Name": i}
            index_types.append(index_type)

        for index_type_data in index_types:
            index_type = IndexType(**index_type_data)
            session.add(index_type)

        # Create default ValueType records
        value_types = []
        for i in config['value_types']:
            value_type = {"Name": i}
            value_types.append(value_type)

        for value_type_data in value_types:
            value_type = ValueType(**value_type_data)
            session.add(value_type)

        # Commit and close the session
        session.commit()
        session.close()
        return ["Database Created Succesfully", None]
    except Exception as _ex:
        logger.critical(_ex)
        return [None, _ex]
