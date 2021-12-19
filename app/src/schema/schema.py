from .schemas import SqliteSchema, BaseSchema


class Schema:
    @staticmethod
    def get_connection() -> BaseSchema:
        return SqliteSchema()
