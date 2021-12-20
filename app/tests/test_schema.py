from app.src.schema.schema import Schema
from app.src.schema.schemas import BaseSchema


class TestSchema:

    def test_schema_connection(self):
        schema: BaseSchema = Schema.get_schema()
        connection = schema.get_connection()
        assert connection

