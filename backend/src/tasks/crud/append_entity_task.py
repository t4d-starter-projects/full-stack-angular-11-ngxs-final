from typing import TypeVar, Generic

from src.core.interfaces.logging import LoggingInterface
from src.core.interfaces.crud import CRUDInterface
from ..task_interface import TaskInterface

EntityType = TypeVar('EntityType')


class AppendEntityTask(TaskInterface[EntityType], Generic[EntityType]):

    def __init__(self, logging: LoggingInterface,
                 entities: CRUDInterface[EntityType]):
        self.logging = logging
        self.entities = entities

    def run(self, entity: EntityType):
        return self.entities.append_one(entity)
