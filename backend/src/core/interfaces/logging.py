import abc


class LoggingInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def info(self, message: str):
        ...

    @abc.abstractmethod
    def error(self, message: str):
        ...
