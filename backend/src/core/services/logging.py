from ..interfaces.logging import LoggingInterface


class Logging(LoggingInterface):

    def __init__(self):
        print('logging instantiated')

    def info(self, message: str) -> None:
        print(message)

    def error(self, message: str) -> None:
        print(message)
