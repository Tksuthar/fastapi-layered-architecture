from typing import Type
import urllib
from abc import ABC

from sqlalchemy import engine
from core.services import Service
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine

from sqlalchemy.orm import sessionmaker, Session


class DatabaseService(Service, ABC):
    def __init__(self, engine: Engine) -> None:
        super().__init__()
        self._engine = engine

    def get_session_maker(self, autocommit=False, autoflush=False) -> Session:
        return sessionmaker(
            autocommit=autocommit, autoflush=autoflush, bind=self._engine
        )


class SQLServerService(DatabaseService):
    def __init__(self, connection_string: str) -> None:
        super().__init__(
            engine=create_engine(
                f"mssql+pyodbc:///?odbc_connect={urllib.parse.quote_plus(connection_string)}",
                connect_args={"check_same_thread": False, "autocommit": True},
            )
        )


class SqlLiteService(DatabaseService):
    def __init__(self, connection_string: str) -> None:
        super().__init__(
            engine=create_engine(
                connection_string, connect_args={"check_same_thread": False}
            )
        )

class MySqlService(DatabaseService):
    def __init__(self, connection_string: str) -> None:
        super().__init__(
            engine=create_engine(
                connection_string, connect_args={"autocommit": True}
            )
        )