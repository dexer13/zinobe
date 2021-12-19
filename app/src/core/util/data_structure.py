import pandas as pd
from typing import List
from pandas import DataFrame
from app.src.schema.schema import Schema


class DataStructure:
    data_frame: DataFrame = None

    def __init__(self, data: List):
        self.data_frame = pd.DataFrame(data)

    def to_json_file(self, path: str):
        self.data_frame.to_json(path, orient='records')

    def save_review(self):
        self.data_frame.to_sql('countries_review', Schema.get_connection())

def say_hello():
    print('Hola denis')