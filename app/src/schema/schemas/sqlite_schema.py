import sqlite3
import pathlib
from sqlite3 import Error, Connection, Cursor
from .base_schema import BaseSchema


class SqliteSchema(BaseSchema):
    connection: Connection = None
    def get_connection(self) -> Connection:
        try:
            database_url: str = \
                f'{pathlib.Path(__file__).parent.parent.absolute()}' \
                f'/db/countries_review.db'
            self.connection = sqlite3.connect(database=database_url)
            print(sqlite3.version)
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

