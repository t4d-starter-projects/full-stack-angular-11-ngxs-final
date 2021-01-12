import abc

from sqlalchemy.orm import sessionmaker


class DataSessionInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get_session(self) -> sessionmaker:
        ...
