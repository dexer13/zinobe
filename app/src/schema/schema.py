from .schemas import SqliteSchema, BaseSchema
from app.config.PARAMETERS import Parameters

class Schema:
    @staticmethod
    def get_schema() -> BaseSchema:
        if Parameters.is_test:
            return SqliteSchema('db_test')
        return SqliteSchema()
