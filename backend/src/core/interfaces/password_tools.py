import abc


class PasswordToolsInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def validate(self, hashed_password: str, password: str) -> bool:
        ...

    @abc.abstractmethod
    def generate_hashed_password(self, password: str) -> str:
        ...
