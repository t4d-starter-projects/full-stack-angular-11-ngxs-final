import abc
from typing import TypeVar, Generic, List, Dict

T = TypeVar('T')


class CRUDInterface(Generic[T], metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def all(self) -> List[T]:
        pass

    @abc.abstractmethod
    def one_by_id(self, entity_id: int) -> T:
        pass

    @abc.abstractmethod
    def append_one(self, entity: Dict) -> T:
        pass

    @abc.abstractmethod
    def replace_one(self, entity: Dict) -> None:
        pass

    @abc.abstractmethod
    def remove_one(self, entity_id: int) -> None:
        pass
