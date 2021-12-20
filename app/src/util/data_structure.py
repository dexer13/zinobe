import pandas as pd
from typing import List
from pandas import DataFrame
from app.src.schema.schema import Schema
from app.src.schema.schemas import BaseSchema


class DataStructure:
    data_frame: DataFrame = None
    table_name: str = None

    def __init__(self, data: List, table_name: str = 'countries_review'):
        self.data_frame = pd.DataFrame(data)
        self.table_name = table_name

    def to_json_file(self, path: str):
        self.data_frame.to_json(path, orient='records')

    def get_review(self):
        review = self.data_frame.agg({
            'time': ['sum', 'mean', 'min', 'max']
        })
        data_structure = DataStructure(review)
        return data_structure

    def save(self) -> bool:
        try:
            schema: BaseSchema = Schema.get_schema()
            connection = schema.get_connection()
            schema.remove_table(self.table_name)
            self.data_frame.to_sql(
                self.table_name, connection
            )
            return True
        except Exception as e:
            return False