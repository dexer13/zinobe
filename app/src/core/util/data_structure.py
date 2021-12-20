import pandas as pd
from typing import List
from pandas import DataFrame
from app.src.schema.schema import Schema
from app.src.schema.schemas import BaseSchema


class DataStructure:
    data_frame: DataFrame = None

    def __init__(self, data: List):
        self.data_frame = pd.DataFrame(data)

    def to_json_file(self, path: str):
        self.data_frame.to_json(path, orient='records')

    def save_review(self):
        schema: BaseSchema = Schema.get_schema()
        connection = schema.get_connection()
        schema.remove_table('countries_review')
        review = self.data_frame.agg({
            'time': ['sum', 'mean', 'min', 'max']
        })
        review.to_sql(
            'countries_review', connection
        )

def say_hello():
    print('Hola denis')