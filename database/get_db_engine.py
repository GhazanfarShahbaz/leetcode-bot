from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from os import environ

from utility.generate_environment import load_environment

load_environment()

def get_engine() -> Engine:
    """
    Creates and returns an SQLAlchemy engine object.

    This function reads environment variables for the connection details to the database and uses
    them to create an SQLAlchemy engine object.

    Returns:
        An SQLAlchemy engine object that can be used to connect to a database.
    """
    
    sql_type: str = environ["SQL_TYPE"]
    sql_host: str = environ["SQL_HOST"]
    sql_password: str = environ["SQL_PASSWORD"]
    sql_port: str = environ["SQL_PORT"]
    sql_database: str = environ["SQL_DATABASE"]
    sql_username: str = environ["SQL_USERNAME"]

    engine: Engine = create_engine(
        f"{sql_type}://{sql_username}:{sql_password}@{sql_host}:{sql_port}/{sql_database}")
    return engine