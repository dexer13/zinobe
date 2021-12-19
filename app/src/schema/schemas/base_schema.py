from abc import ABC, abstractmethod


class BaseSchema(ABC):

    @abstractmethod
    def get_connection(self):
        pass
