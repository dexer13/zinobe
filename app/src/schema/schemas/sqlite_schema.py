import sqlite3
import pathlib
from sqlite3 import Error, Connection, Cursor
from .base_schema import BaseSchema


class SqliteSchema(BaseSchema):
    connection: Connection = None

    def __init__(self, database_name: str = 'countries_review'):
        try:
            database_url: str = \
                f'{pathlib.Path(__file__).parent.parent.absolute()}' \
                f'/db/{database_name}.db'
            self.connection = sqlite3.connect(database=database_url)
        except Error as e:
            print(e)

    def get_connection(self) -> Connection:
        try:
            return self.connection
        except Error as e:
            print(e)

    def remove_table(self, table_name: str):
        try:
            cursor: Cursor = self.connection.cursor()
            cursor.execute(f'DROP TABLE {table_name}')
            self.connection.commit()
        except Error as e:
            print(e)

