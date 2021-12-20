from .schemas import SqliteSchema, BaseSchema


class Schema:
    @staticmethod
    def get_schema() -> BaseSchema:
        return SqliteSchema()
