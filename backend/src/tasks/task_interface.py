import abc
from typing import TypeVar, Generic

TaskResultType = TypeVar('TaskResultType')


class TaskInterface(Generic[TaskResultType], metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def run(self, *args) -> TaskResultType:
        ...
