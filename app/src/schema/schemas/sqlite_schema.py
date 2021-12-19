import sqlite3
import pathlib
from sqlite3 import Error, Connection
from .base_schema import BaseSchema


class SqliteSchema(BaseSchema):
    def get_connection(self) -> Connection:
        try:
            database_url: str = \
                f'{pathlib.Path(__file__).parent.parent.absolute()}' \
                f'/db/countries_review.db'
            connection: Connection = sqlite3.connect(database=database_url)
            print(sqlite3.version)
            return connection
        except Error as e:
            print(e)
