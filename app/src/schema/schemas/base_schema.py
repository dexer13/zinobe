from abc import ABC, abstractmethod


class BaseSchema(ABC):

    @abstractmethod
    def get_connection(self):
        pass

    @abstractmethod
    def remove_table(self, table_name: str):
        pass
